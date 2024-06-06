from fastapi import BackgroundTasks, FastAPI, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
import spacy

from .database import async_get_db

from .crud import crud_episode, crud_title

from .models.title import TitleBase

async def generate_keywords(title_id: int, db: AsyncSession = Depends(async_get_db)):
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
    keywords = ",".join({ent.text for ent in doc.ents})

    # save the string of entities to keywords column in the title table
    await crud_title.update(db, id=title_id, object=TitleBase(
        name=title["name"],
        num_seasons=title["num_seasons"],
        synopsis=title["synopsis"],
        keywords=keywords
    ))

    return keywords # for testing

def calculate_reliability_score(candidate_text, title_keywords):
    # run NER on candidate_text to get candidate_keywords
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(candidate_text)
    candidate_keywords = ",".join(set([ent.text for ent in doc.ents]))
    print("Candidate keywords:", candidate_keywords)

    # calculate the intersection between candidate_keywords and title_keywords
    intersection = set(candidate_keywords.split(",")) & set(title_keywords.split(","))

    # return the intersection / candidate_keywords.size()
    return len(intersection) / len(candidate_keywords.split(","))