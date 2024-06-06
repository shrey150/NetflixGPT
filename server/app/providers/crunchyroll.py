from celery import chain, group
from fastapi import BackgroundTasks, HTTPException
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession

from app.tasks import find_fandom_sub, process_episode

from ..models.episode import EpisodeCreate
from ..models.title import TitleCreate

from ..models.crunchyroll import CrunchyPayload
from ..models.crunchyroll import EpisodeData as CrunchyrollEpisode
from ..models.metadata import MetadataRequest
from ..crud import crud_episode, crud_title

from ..ner import generate_keywords

def find_crunchyroll_episode(data: CrunchyPayload) -> (CrunchyrollEpisode, int, int):
    for season_num, season in enumerate(data.seasons):
        print("season_num", season_num)
        for ep_num, episode in enumerate(season.data):
            print("ep_num", ep_num)
            print(episode.id, data.current_episode, data.lang)
            for v in episode.versions:
                if v.audio_locale == data.lang and v.guid == data.current_episode:
                    print("found episode")
                    return (episode, season_num+1, ep_num+1)

    raise HTTPException(status_code=400, detail="Episode metadata not found in Crunchyroll payload")

async def ensure_all_episodes_in_db_crunchy(data: CrunchyPayload, db: AsyncSession, title_id: int):
    parallel_scraper_tasks = []
    title = await crud_title.get(db, id=title_id)
    for season_num, season in enumerate(data.seasons):
        for ep_num, episode in enumerate(season.data):
            episode_name = episode.title
            if not await crud_episode.exists(db, name=episode_name, title_id=title_id):
                print("Discovered episode", episode_name)
                await crud_episode.create(db, object=EpisodeCreate(
                    name=episode_name,
                    synopsis=episode.description,
                    title_id=title_id,
                    # account for zero-indexing -> 1-indexing
                    season_num=season_num+1,
                    ep_num=ep_num+1,
                ))

                episode = await crud_episode.get(db, name=episode_name, title_id=title_id)
                parallel_scraper_tasks.append(process_episode(title, episode))
    
    # execute all tasks in parallel
    chain(
        find_fandom_sub.s(title),
        group(parallel_scraper_tasks),
    ).delay()

    await generate_keywords(title_id, db)

async def resolve_crunchyroll(
    payload: MetadataRequest,
    background_tasks: BackgroundTasks,
    db: AsyncSession
):
    try:
        data = CrunchyPayload(**payload.data)
    except ValidationError as e:
        print(e)
        raise HTTPException(status_code=400, detail="Malformed Netflix metadata") from e
    title_name = data.title
    num_seasons = len(data.seasons)
    synopsis = data.synopsis

    if not await crud_title.exists(db, name=title_name):
        print(f"Discovered title {title_name}")
        await crud_title.create(db, object=TitleCreate(
            name=title_name,
            num_seasons=num_seasons,
            synopsis=synopsis,
        ))

    title = await crud_title.get(db, name=title_name)
    crunchyroll_episode, season_num, ep_num = find_crunchyroll_episode(data)
    episode_name = crunchyroll_episode.title

    if not await crud_episode.exists(db, name=episode_name):
        print(f"Discovered episode {episode_name}")
        await crud_episode.create(db, object=EpisodeCreate(
            name=episode_name,
            synopsis=crunchyroll_episode.description,
            season_num=season_num,
            ep_num=ep_num,
            title_id=title["id"])
        )

    episode = await crud_episode.get(db, name=episode_name)
    background_tasks.add_task(ensure_all_episodes_in_db_crunchy, data, db, title["id"])

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