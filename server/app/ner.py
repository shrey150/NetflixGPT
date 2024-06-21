from collections import Counter

from fastapi import BackgroundTasks, FastAPI, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
import spacy

from .database import async_get_db

from .crud import crud_episode, crud_title

from .models.title import TitleBase
from .models.episode import Episode

async def generate_keywords(title_id: int, db: AsyncSession = Depends(async_get_db)) -> dict[str, float]:
    # get title
    title = await crud_title.get(db, id=title_id)

    #get all synopses from episodes and title if exists
    episodes = await crud_episode.get_multi(db, title_id=title_id)
    all_synopses = title["synopsis"] if title["synopsis"] else ""
    for episode in episodes['data']:
        all_synopses += " " + episode["synopsis"]

    # concatenate all the synopses and pass it to the NER model
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(all_synopses)

    # combine entities
    keywords = [ent.text for ent in doc.ents]

    # calculate frequencies
    keyword_frequencies = Counter(keywords)

    # save the string of entities to keywords column in the title table
    await crud_title.update(db, id=title_id, object=TitleBase(
        name=title["name"],
        num_seasons=title["num_seasons"],
        synopsis=title["synopsis"],
        keywords=dict(keyword_frequencies)
    ))

    return keyword_frequencies # for testing

def normalize_frequencies(frequencies: dict[str, int]) -> dict[str, float]:
    max_freq = max(frequencies.values(), default=1)
    keyword_weights = {k: v / max_freq for k, v in frequencies.items()}
    return keyword_weights

def weight_keywords(keywords: list[str], weights: dict[str, float]) -> dict[str, float]:
    weighted_keywords = {}
    for keyword in keywords:
        keyword = keyword.strip()
        weighted_keywords[keyword] = weights.get(keyword, 0.1)
    return weighted_keywords

def calculate_reliability_score(candidate_text: str, title_keywords: dict[str, float]) -> float:
    # run NER on candidate_text to get candidate_keywords
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(candidate_text)
    candidate_keywords = set(ent.text for ent in doc.ents)

    # normalize and weight the keywords by the synopses frequencies
    keyword_weights = normalize_frequencies(title_keywords)
    weighted_title_keywords = weight_keywords(title_keywords.keys(), keyword_weights)
    weighted_candidate_keywords = weight_keywords(candidate_keywords, keyword_weights)

    # calculate the weighted IOC score
    intersection_weight = sum(weighted_title_keywords.get(keyword, 0) for keyword in candidate_keywords)
    candidate_weight = sum(weighted_candidate_keywords.values())

    return intersection_weight / candidate_weight if candidate_weight > 0 else 0.0

def search_rules_generator(episode: Episode, source: str, streaming_provider: str = "netflix"):
    # Crunchyroll overrides source rules
    if streaming_provider == "crunchyroll":
        search_sequence = [] # TODO: implement crunchyroll search rules
    else:
        if source == "fandom":
            search_sequence = [f'"{episode.name}"', episode.name, f'Season {episode.season_num} Episode {episode.ep_num}']
        elif source == "wikipedia":
            search_sequence = [f'"{episode.name}"', f'{episode.name} ([Show name])'] # TODO: put show name
        else:
            search_sequence = [] # TODO: implement other source search rules

    for item in search_sequence:
        yield item