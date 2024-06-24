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

from .crud import crud_title_source, crud_source, crud_summary, crud_title

from .ner import calculate_reliability_score, search_rules_generator

from config import settings, SUMMARY_RELIABILITY_THRESHOLD
from sentence_transformers import SentenceTransformer

from .vecstore import text_splitter, embeddings, index

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
                reliability_score=0.0
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
def scrape_episode_fandom(payload: dict, episode: dict, search_term: str) -> SummaryCreate:
    episode: Episode = Episode(**episode)
    payload: FandomSubPayload = FandomSubPayload(**payload)

    # Set up the custom site configuration
    config.family_files[payload.sub] = f'https://{payload.sub}.fandom.com/api.php'
    site = pywikibot.Site(payload.sub, payload.sub)

    # Using given search term, get first result
    try:
        # TODO: this may only work for Fandom
        search_results = list(pagegenerators.SearchPageGenerator(search_term, site=site, total=1, namespaces=[0]))
        page = search_results[0] if search_results else None
        if page is None:
            raise StopIteration

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

    # is this necessary?
    except StopIteration:
        # page generator failed, return empty text
        return FandomScraperPayload(
            sub=payload.sub,
            source_id=payload.source_id,
            title_id=payload.title_id,
            raw_text='',
            url=url,
            ep_id=episode.id
        ).model_dump()

@app.task
def summarize_episode_fandom(payload: dict) -> SummaryCreate:
    return async_to_sync(summarize_episode_fandom_async)(payload)

async def summarize_episode_fandom_async(payload: dict) -> SummaryCreate:
    payload: FandomScraperPayload = FandomScraperPayload(**payload)
    soup = BeautifulSoup(payload.raw_text, 'html5lib')

    # Using CSS selectors to get all p tags that are children of mw-parser-output
    # TODO can optimize by only selecting p tags that are directly adjacent to h2s containing "Story|Synopsis|Plot|Summary|Story"
    paragraphs = soup.select('.mw-parser-output > p')
    text = ' '.join(p.get_text() for p in paragraphs)

    # calculate NER score for this summary
    async for db in async_get_db():
        title = await crud_title.get(db, title_id=payload.title_id)
        title_keywords = title['keywords']
        reliability_score = calculate_reliability_score(text, title_keywords)

    summary_create = SummaryCreate(
        sub=payload.sub,
        source_id=payload.source_id,
        title_id=payload.title_id,
        raw_text=payload.raw_text,
        url=payload.url,
        ep_id=payload.ep_id,
        text=text,
        reliability_score=reliability_score,
        is_primary=False,
    )

    return summary_create.model_dump()

@app.task
async def write_summary_to_db(summary: SummaryCreate) -> Summary:
    async for db in async_get_db():
        await crud_summary.create(db, object=summary)

@app.task
def index_episode(payload: dict):
    payload: FandomSummaryPayload = FandomSummaryPayload(**payload)

    docs = text_splitter.create_documents([payload.text])
    embedding_metadata_pairs = []

    for i, doc in enumerate(docs):
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

            embedding_id = f"{payload.sub}-{payload.source_id}-{payload.title_id}-{payload.ep_id}-{i}"
            embedding_metadata_pairs.append((embedding_id, embedding, metadata))

        except Exception as e:
            print(f"Error indexing document at index {i}: {e}")

    if embedding_metadata_pairs:
        try:
            index.upsert(embedding_metadata_pairs)
        except Exception as e:
            print(f"Error during upsert operation: {e}")

    return {"status": "indexed"}

@app.task(bind=True)
async def feedback_loop(title: dict, episode: dict, search_term_generator: tuple) -> Summary:
    search_list, idx = search_term_generator

    if idx >= len(search_list):
        print("All search attempts exhausted, using episode synopsis fallback...")
        summary_create = SummaryCreate(
            sub=None,
            source_id=-1,
            title_id=title.id,
            raw_text=episode.synopsis,
            url=None,
            ep_id=episode.id,
            text=episode.synopsis,
            reliability_score=1.0,
            is_primary=False,
        )
        return await write_summary_to_db(summary_create)
    
    search_term = search_list[idx]
    print("Search term:", search_term)

    # Continue with the scraping, summarizing, and validation process
    return chain(
        scrape_episode_fandom.s(episode, search_term),
        summarize_episode_fandom.s(),
        validate_summary.s(title, episode, search_term_generator)
    ).apply_async()

@app.task(bind=True)
def validate_summary(payload: dict, title: dict, episode: dict, search_term_generator: tuple) -> dict:
    payload: SummaryCreate = SummaryCreate(**payload)
    reliability_score = payload.reliability_score
    search_list, idx = search_term_generator

    if reliability_score >= SUMMARY_RELIABILITY_THRESHOLD:
        print(f'Indexing {episode.name} with score {reliability_score}...')
        return chain(
            write_summary_to_db.s(payload.model_dump()),
            index_episode.s(payload.model_dump())
        ).apply_async()
    else:
        print(f'Retrying {episode.name} with score {reliability_score}...')
        return feedback_loop.s(title, episode, (search_list, idx + 1)).apply_async()


# entry point for our processing pipeline
def process_episode(title: dict, episode: dict):
    search_term_list = list(search_rules_generator(Episode(**episode), 'fandom'))
    search_term_generator = (search_term_list, 0)
    print("Pseudo-generator:", search_term_generator)
    return feedback_loop.s(title, episode, search_term_generator)
    # return chain(
        # scrape_episode_fandom.s(episode),
        # summarize_episode_fandom.s(),
        # index_episode.s(),
    # )
