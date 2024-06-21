from celery import chain, group
from fastapi import BackgroundTasks, HTTPException
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession

from app.tasks import find_fandom_sub, process_episode

from ..models.episode import EpisodeCreate
from ..models.title import TitleCreate

from ..models.netflix import NetflixPayload
from ..models.netflix import Episode as NetflixEpisode
from ..models.metadata import MetadataRequest
from ..crud import crud_episode, crud_title

from ..ner import generate_keywords

def find_netflix_episode(data: NetflixPayload) -> (NetflixEpisode, int, int):
    for season_num, season in enumerate(data.video.seasons):
        for ep_num, episode in enumerate(season.episodes):
            if episode.episodeId == data.video.currentEpisode:
                # convert from zero-indexing to 1-indexing
                return (episode, season_num+1, ep_num+1)

    raise HTTPException(status_code=400, detail="Episode metadata not found in Netflix payload")

async def ensure_all_episodes_in_db(data: NetflixPayload, db: AsyncSession, title_id: int):
    parallel_scraper_tasks = []
    
    print(f'Ensuring all episodes exist for title id {title_id}')
    title = await crud_title.get(db, id=title_id)

    abs_ep_count = 1
    for season_num, season in enumerate(data.video.seasons):
        for ep_num, netflix_episode in enumerate(season.episodes):
            episode_name = netflix_episode.title
            if not await crud_episode.exists(db, name=episode_name, title_id=title_id):
                print(f'Discovered episode {episode_name}')
                episode = await crud_episode.create(db, object=EpisodeCreate(
                    name=episode_name,
                    synopsis=netflix_episode.synopsis,
                    title_id=title_id,
                    abs_ep_num = abs_ep_count,
                    # account for zero-indexing -> 1-indexing
                    season_num=season_num+1,
                    ep_num=ep_num+1,
                ))
                abs_ep_count += 1

            episode = await crud_episode.get(db, name=episode_name, title_id=title_id)
            parallel_scraper_tasks.append(process_episode(title, episode))

    await generate_keywords(title_id, db)

    if len(parallel_scraper_tasks) > 0:
        # execute all tasks in parallel    
        chain(
            find_fandom_sub.s(title),
            group(parallel_scraper_tasks),
        ).delay()

async def resolve_netflix(
    payload: MetadataRequest,
    background_tasks: BackgroundTasks,
    db: AsyncSession
):
    try:
        data = NetflixPayload(**payload.data)
    except ValidationError as e:
        print(e)
        raise HTTPException(status_code=400, detail="Malformed Netflix metadata") from e

    title_name = data.video.title
    num_seasons = len(data.video.seasons)
    synopsis = data.video.synopsis

    if not await crud_title.exists(db, name=title_name):
        print(f"Discovered title {title_name}")
        title = await crud_title.create(db, object=TitleCreate(
            name=title_name,
            num_seasons=num_seasons,
            synopsis=synopsis,
        ))

        # find_fandom_sub.s(title.model_dump())

    title = await crud_title.get(db, name=title_name)

    netflix_episode, season_num, ep_num = find_netflix_episode(data)
    episode_name = netflix_episode.title

    if not await crud_episode.exists(db, name=episode_name, title_id=title['id']):
        print(f"Discovered episode {episode_name}")
        await crud_episode.create(db, object=EpisodeCreate(
            name=episode_name,
            synopsis=netflix_episode.synopsis,
            season_num=season_num,
            ep_num=ep_num,
            title_id=title["id"])
        )

    episode = await crud_episode.get(db, title_id=title['id'])
    background_tasks.add_task(ensure_all_episodes_in_db, data, db, title["id"])

    # include title & episode objects in final response
    res = {
        "episode_id": episode["id"],
        "episode_name": episode["name"],
        "title_name": title["name"],
        "title_id": title["id"],
        **title,
        **episode,
    }

    # account for key collisions
    res.pop("id")
    res.pop("name")

    return res