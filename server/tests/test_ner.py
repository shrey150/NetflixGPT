import spacy
import asyncio
from app.server import generate_keywords
from app.database import async_get_db, get_engine
from sqlalchemy.ext.asyncio import AsyncSession

def calculate_reliability_score(candidate_text, title_keywords):
    # run NER on candidate_text to get candidate_keywords
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(candidate_text)
    candidate_keywords = ", ".join(set([ent.text for ent in doc.ents]))
    print("Candidate keywords:", candidate_keywords)

    # calculate the intersection between candidate_keywords and title_keywords
    intersection = set(candidate_keywords.split(", ")) & set(title_keywords.split(", "))

    # return the intersection / candidate_keywords.size()
    return len(intersection) / len(candidate_keywords.split(", "))

def test_calculate_reliability_score():
    print("testing reliability score...")
    candidate_text = "When Sebastian Thrun started working on self-driving cars at Google in 2007, few people outside of the company took him seriously. “I can tell you very senior CEOs of major American car companies would shake my hand and turn away because I wasn’t worth talking to,” said Thrun, in an interview with Recode earlier this week."
    title_keywords = "Sebastian Thrun, self-driving cars, Google, 2007, car companies, CEOs, major American"
    print(calculate_reliability_score(candidate_text, title_keywords))

async def test_generate_keywords():
    print("testing generate_keywords on Better Call Saul...")
    title_id = 1 # better call saul ID

    async with AsyncSession(get_engine()) as db:
        keywords = await generate_keywords(title_id, db)
        print("Keywords:", keywords)

def main():
    test_calculate_reliability_score()
    asyncio.run(test_generate_keywords())

if __name__ == "__main__":
    main()