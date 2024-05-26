from bs4 import BeautifulSoup
from celery import Celery
import requests
import pywikibot
from pywikibot import pagegenerators, config
from bs4 import BeautifulSoup
from sqlalchemy.ext.asyncio import AsyncSession

from .models.episode import EpisodeBase
from .models.summary import SummaryBase
from .models.title import TitleBase
from .models.source import SourceCreate, SourceType
from .models.title_source import TitleSourceCreate

from .crud import crud_title_source
from .crud import crud_source

from config import settings

# app = Celery('tasks', broker=settings.REDIS_QUEUE_URI)

async def find_fandom_sub(title: TitleBase, db: AsyncSession) -> str:
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
        title_source = await crud_title_source.get(db, title_id=title.id)
        source = await crud_source.get(db, source_id=title_source['source_id'])
        fandom_sub_url = source['url']

    print(f'Fandom URL: {fandom_sub_url}')
    return fandom_sub_url

async def scrape_episode_fandom(episode: EpisodeBase, sub: str) -> SummaryBase:

    # Set up the custom site configuration
    config.family_files[sub] = f'https://{sub}.fandom.com/api.php'
    site = pywikibot.Site(sub, sub)

    search_results = pagegenerators.SearchPageGenerator(episode.name, site=site, total=1)

    # Get the first page from the search results
    page = next(search_results)
    print('Scraping page: ', page.title())

    # infer URL name from page title
    # TODO: ideally get URL from page data, this works for now
    url = f'https://{sub}.fandom.com/wiki/{page.title().replace(" ", "_")}'

    response = requests.get(url, timeout=5)
    response.raise_for_status()

    return response.text


# @app.task
def summarize_episode(raw_text: str):
    soup = BeautifulSoup(raw_text, 'html5lib')

    # Using CSS selectors to get all p tags that are children of mw-parser-output
    # TODO can optimize by only selecting p tags that are directly adjacent to h2s containing "Story|Synopsis|Plot|Summary|Story"
    paragraphs = soup.select('.mw-parser-output > p')
    text_content = ' '.join(p.get_text() for p in paragraphs)
    return text_content

# @app.task
def index_episode(summarized_data):
    # Index the episode
    indexed_data = {'episode_id': summarized_data['episode_id'], 'index': '...'}
    return indexed_data
