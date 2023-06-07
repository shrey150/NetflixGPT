import pywikibot
from pywikibot import pagegenerators, config
import mwparserfromhell
from langchain import SerpAPIWrapper
import re

class Scraper():
    def __init__(self):
        config.family_files['netflix'] = 'https://netflix.fandom.com/api.php'
        self.searcher = SerpAPIWrapper()

    def get_fandom_sub(self, title) -> str:
        data = self.searcher.results(f"{title} fandom")
        search_result = data['organic_results'][0]['link']
        sub = search_result.split('.')[0].split('//')[1]

        api_url = f'https://{sub}.fandom.com/api.php'
        config.family_files[sub] = f'https://{sub}.fandom.com/api.php'
        print('Added scraper source: ', api_url)

        # TODO: save all config familes to disk & load on startup
        return sub
    
    def fetch(self, title, ep_title) -> str:
        search_terms = [
            f"\"{ep_title}\"",
            f"\"{ep_title} ({title})\"",
        ]

        custom_sub = self.get_fandom_sub(title)

        sites = [
            pywikibot.Site(custom_sub, custom_sub),
            pywikibot.Site("en", "wikipedia"),
            pywikibot.Site("en", "netflix"),
        ]

        # try to fetch plot from fandom, wikipedia, and netflix
        # return whichever summary is longest

        sources = []

        # find most relevant plot section on each source
        for site in sites:
            print('Searching site: ', site)
            results = list(map(lambda term: self._fetch_plot(site, term), search_terms))
            results = list(filter(lambda result: result is not None, results))

            if len(results) > 0:
                sources.append(max(results, key=len))

        # return longest plot source
        if len(sources) > 0:
            plot = max(sources, key=len)
            print('Found plot:', plot)
            return plot
        
        # TODO finally try GPT search

    # generic scraper that takes in specific site/search term format
    # returns the plot text if it finds it, otherwise returns None
    def _fetch_plot(self, site, search_term, heading_names=['Plot', 'Synopsis', 'Summary']):
        search_results = pagegenerators.SearchPageGenerator(search_term, site=site, total=1)

        page = next(search_results)
        print('Scraping page: ', page.title())

        wikicode = mwparserfromhell.parse(page.text)

        # Still doesn't work for Ozymandias
        pattern = r"\s*(?i:Plot|Summary|Main\s+story)\s*"
        sections = wikicode.get_sections(matches=pattern,include_lead=True)
       
        if len(sections) > 0:
            plot = max(sections, key=lambda x: len(x))
            print(f'Found plot section: \n\"{plot}\"')
            return plot