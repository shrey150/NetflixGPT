import asyncio
from bs4 import BeautifulSoup
from celery import Celery, chain
from fastapi import BackgroundTasks, Depends
from langchain_text_splitters import RecursiveCharacterTextSplitter
import requests
import pywikibot
from pywikibot import pagegenerators, config
from bs4 import BeautifulSoup
from sqlalchemy.ext.asyncio import AsyncSession
from asgiref.sync import async_to_sync
import tldextract
from pinecone import Pinecone, ServerlessSpec

from .models.scraper import FandomScraperPayload, FandomSubPayload, FandomSummaryPayload

from .database import async_get_db

from .models.episode import Episode, EpisodeBase
from .models.summary import SummaryBase, SummaryCreate, Summary
from .models.title import TitleBase, Title
from .models.source import SourceCreate, SourceType, Source
from .models.title_source import TitleSourceCreate

from .crud import crud_title_source, crud_source, crud_summary

from config import settings
from sentence_transformers import SentenceTransformer

app = Celery('tasks', broker=settings.REDIS_QUEUE_URI)
embeddings = SentenceTransformer('all-mpnet-base-v2')

# Initialize Pinecone
pinecone = Pinecone(api_key=settings.PINECONE_API_KEY)
index_name = "netflixgpt"
if index_name not in pinecone.list_indexes().names():
    pinecone.create_index(
        name=index_name,
        dimension=768,
        spec=ServerlessSpec(cloud='aws', region='us-east-1'),
    )
index = pinecone.Index(index_name)

text_splitter = RecursiveCharacterTextSplitter(
    separators=[
        "\n\n",
        "\n",
        " ",
        ".",
        ",",
        "\u200b",  # Zero-width space
        "\uff0c",  # Fullwidth comma
        "\u3001",  # Ideographic comma
        "\uff0e",  # Fullwidth full stop
        "\u3002",  # Ideographic full stop
        "",
    ],
    chunk_size=100,
    chunk_overlap=0
)

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

        # TODO this assumes 1:1 relationship between title and source
        # expand this when we support TVTropes, Wikipedia, IMDB, Reddit, etc.

        print('we reach here')
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
                # TODO convert to `logging.warn()``
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

        # NOTE: this is sometimes happening -- probably when two `process_episode` chains are started
        # So if an exception is raised, it actually is helping us flag repeated first scrape attempts
        # TODO validate that this is true and if so, gracefully handle the error instead of "this should never happen"
        else:
            print('this is the issue')
            raise Exception('find_fandom_sub called on title associated with an existing Fandom source')

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

    """
    TODO: have a series of fallbacks for finding an episode.
    1) episode.name
    2) f'"{episode.name}"'
    3) f'Episode {num}'     <-- will likely require `episodes.absolute_ep_num` column,
                                maybe `episodes.display_num` for edge case w/ 0.5s
    """

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

    return FandomSummaryPayload(
        sub=payload.sub,
        source_id=payload.source_id,
        title_id=payload.title_id,
        raw_text=payload.raw_text,
        url=payload.url,
        ep_id=payload.ep_id,
        text=text,
    ).model_dump()

async def write_summary_to_db(summary: SummaryCreate) -> Summary:
    async for db in async_get_db():
        await crud_summary.create(db, object=summary)

@app.task
def index_episode(payload: dict):
    payload: FandomSummaryPayload = FandomSummaryPayload(**payload)

    docs = text_splitter.create_documents([payload.text])

    for doc in docs:
        try:
            embedding = embeddings.encode(doc.page_content)
            metadata = {
                'sub': payload.sub,
                'source_id': payload.source_id,
                'title_id': payload.title_id,
                'ep_id': payload.ep_id,
                'text': doc.page_content,
                'url': payload.url,
            }
            index.upsert([(f"{payload.ep_id}_{i}", embedding, metadata) for i, _ in enumerate(docs)])
        except Exception as e:
            print(f"Error indexing document: {e}")

    return {"status": "indexed"}

# entry point for our processing pipeline
def process_episode(title, episode):
    return chain(
        scrape_episode_fandom.s(episode),
        summarize_episode_fandom.s(),
        index_episode.s(),
    )
