from bs4 import BeautifulSoup
from celery import Celery
import requests

from .models.title import TitleBase
from config import settings

app = Celery('tasks', broker=settings.REDIS_QUEUE_URI)

@app.task
def find_fandom_sub(title: TitleBase) -> str:
    base_url = "https://community.fandom.com/wiki/Special:SearchCommunity"
    params = { 'query': title.name }
    response = requests.get(base_url, params=params)

    if response.status_code != 200:
        print(f"Failed to retrieve data: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    # this selects all possible search results
    els = soup.select('.unified-search__result__title')

    '''
    (1) iterate through all search results (if more than one)
    (2) request the text for the home page (the link for the search result) using results
    (3) use BS to parse the home page and get all the text
    (4) perform NER to get all the proper noun keywords like characters, locations, etc (using spaCy)
    (5) if the number of characters in the NER is greater than a certain threshold, return the link

    side note, you also need to get all the text from all the synposes for every episode
    from the show & the show's synopsis and perform NER. these are your ground truth tokens

    now compare how many of the tokens from the fandom sub match, if high enough threshold, you can return it

    keep in mind for some shows there might not be a fandom. if threshold isn't reached, then return None
    '''

    if len(els) > 0:
        print(f"[WARN] multiple Fandom subs found for {title.name}")
        print(f"Assuming first one is best choice: {els[0]['href']}")

    # TODO: don't trust this assumption long-term
    link = els[0]['href']

    return link

# @app.task
# def scrape_episode(episode_id):
#         search_terms = [
#             f"\"{info.ep_title}\"",
#             f"\"{info.ep_title} ({info.title})\"",
#         ]

#         custom_sub = self.get_fandom_sub(info.title)

#         sites = [
#             pywikibot.Site(custom_sub, custom_sub),
#             pywikibot.Site("en", "wikipedia"),
#             pywikibot.Site("en", "netflix"),
#         ]

#         # try to fetch plot from fandom, wikipedia, and netflix
#         # return whichever summary is longest

#         sources = []

#         # find most relevant plot section on each source
#         for site in sites:
#             print('Searching site: ', site)
#             for term in search_terms:
#                 fetched_plot = self._fetch_plot(site, term, info)
#                 if fetched_plot is not None:
#                     return fetched_plot
#     return episode_data

@app.task
def summarize_episode(episode_data):
    # Summarize the episode
    summarized_data = {'episode_id': episode_data['episode_id'], 'summary': '...'}
    return summarized_data

@app.task
def index_episode(summarized_data):
    # Index the episode
    indexed_data = {'episode_id': summarized_data['episode_id'], 'index': '...'}
    return indexed_data

if __name__ == '__main__':
    find_fandom_sub(None)