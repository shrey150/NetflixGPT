import asyncio
from bs4 import BeautifulSoup
from celery import Celery
from fastapi import BackgroundTasks, Depends
import requests
import pywikibot
from pywikibot import pagegenerators, config
from bs4 import BeautifulSoup
from sqlalchemy.ext.asyncio import AsyncSession
from asgiref.sync import async_to_sync
import tldextract

from .models.scraper import FandomScraperPayload, FandomSubPayload

from .database import async_get_db

from .models.episode import Episode, EpisodeBase
from .models.summary import SummaryBase, SummaryCreate, Summary
from .models.title import TitleBase, Title
from .models.source import SourceCreate, SourceType, Source
from .models.title_source import TitleSourceCreate

from .crud import crud_title_source, crud_source, crud_summary

from config import settings

app = Celery('tasks', broker=settings.REDIS_QUEUE_URI)

@app.task
def find_fandom_sub(
    title: dict,
) -> FandomSubPayload:
    result = async_to_sync(find_fandom_sub_async)(title)
    return result

async def find_fandom_sub_async(
    title: dict,
) -> FandomSubPayload:
    title: Title = Title(**title)
    
    async for db in async_get_db():
        print('Finding fandom sub')
        fandom_sub_url = None

        if not await crud_title_source.exists(db, title_id=title.id):
            print('Creating relationship b/t title and source')
            base_url = "https://community.fandom.com/wiki/Special:SearchCommunity"
            params = { 'query': title.name }

            response = requests.get(base_url, params=params, timeout=5)
            response.raise_for_status()

            # fetch all search result elements
            soup = BeautifulSoup(response.text, 'html.parser')
            els = soup.select('.unified-search__result__title')

            # TODO: don't trust this assumption long-term -- verify each sub using NER
            fandom_sub_url = els[0]['href']

            if len(els) > 0:
                print(f"[WARN] multiple Fandom subs found for {title.name}")
                print(f"Assuming first one is best choice: {fandom_sub_url}")

            print(f'Best choice: {fandom_sub_url}')

            source = await crud_source.create(db, object=SourceCreate(
                url=fandom_sub_url,
                type=SourceType.FANDOM,
            ))

            await crud_title_source.create(db, object=TitleSourceCreate(
                title_id=title.id,
                source_id=source.id,
            ))

        else:
            raise Exception('this should never happen')
            title_source = await crud_title_source.get(db, title_id=title.id)
            source = Source(**await crud_source.get(db, source_id=title_source['source_id']))
            fandom_sub_url = source.url

        print(f'Fandom URL: {fandom_sub_url}')
        site_info = tldextract.extract(fandom_sub_url)

        return FandomSubPayload(
            sub=site_info.subdomain,
            source_id=source.id,
            title_id=title.id,
        ).model_dump()

@app.task
def scrape_episode_fandom(payload: dict, episode: dict) -> SummaryCreate:
    episode: Episode = Episode(**episode)
    payload: FandomSubPayload = FandomSubPayload(**payload)

    # Set up the custom site configuration
    config.family_files[payload.sub] = f'https://{payload.sub}.fandom.com/api.php'
    site = pywikibot.Site(payload.sub, payload.sub)

    search_results = pagegenerators.SearchPageGenerator(episode.name, site=site, total=1)

    # Get the first page from the search results
    page = next(search_results)
    print('Scraping page: ', page.title())

    # infer URL name from page title
    # TODO: ideally get URL from page data, this works for now
    url = f'https://{payload.sub}.fandom.com/wiki/{page.title().replace(" ", "_")}'

    response = requests.get(url, timeout=5)
    response.raise_for_status()

    return FandomScraperPayload(
        sub=payload.sub,
        source_id=payload.source_id,
        title_id=payload.title_id,
        raw_text=response.text,
        url=url,
        ep_id=episode.id,
    ).model_dump()

@app.task
def summarize_episode_fandom(payload: dict) -> Summary:
    payload: FandomScraperPayload = FandomScraperPayload(**payload)
    soup = BeautifulSoup(payload.raw_text, 'html5lib')

    # Using CSS selectors to get all p tags that are children of mw-parser-output
    # TODO can optimize by only selecting p tags that are directly adjacent to h2s containing "Story|Synopsis|Plot|Summary|Story"
    paragraphs = soup.select('.mw-parser-output > p')
    text = ' '.join(p.get_text() for p in paragraphs)

    summary_create = SummaryCreate(
        sub=payload.sub,
        source_id=payload.source_id,
        title_id=payload.title_id,
        raw_text=payload.raw_text,
        url=payload.url,
        ep_id=payload.ep_id,
        text=text,
    )

    async_to_sync(write_summary_to_db)(summary_create)

async def write_summary_to_db(summary: SummaryCreate) -> Summary:
    async for db in async_get_db():
        return await crud_summary.create(db, object=summary)

# @app.task
def index_episode(summarized_data):
    # Index the episode
    indexed_data = {'episode_id': summarized_data['episode_id'], 'index': '...'}
    return indexed_data
