import spacy

def calculate_reliability_score(candidate_text, title_keywords):
    # run NER on candidate_text to get candidate_keywords
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(candidate_text)
    candidate_keywords = ", ".join(set([ent.text for ent in doc.ents]))

    # calculate the intersection between candidate_keywords and title_keywords
    intersection = set(candidate_keywords.split(", ")) & set(title_keywords.split(", "))

    # return the intersection / candidate_keywords.size()
    return len(intersection) / len(candidate_keywords.split(", "))