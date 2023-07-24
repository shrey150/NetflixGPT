import pickle
import pywikibot
from pywikibot import pagegenerators, config
import mwparserfromhell
from langchain import SerpAPIWrapper
import re

from langchain.prompts import load_prompt
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain import PromptTemplate, LLMChain

from langchain.chat_models import ChatOpenAI
# from langchain.chains import create_extraction_chain, create_extraction_chain_pydantic
# from langchain.prompts import ChatPromptTemplate

from constants import *

class Scraper():
    def __init__(self):
        config.family_files['netflix'] = 'https://netflix.fandom.com/api.php'
        self.searcher = SerpAPIWrapper()
        self._load_sources_from_disk()

    def get_fandom_sub(self, title) -> str:
        data = self.searcher.results(f"{title} fandom")
        search_result = data['organic_results'][0]['link']
        sub = search_result.split('.')[0].split('//')[1]

        api_url = f'https://{sub}.fandom.com/api.php'
        config.family_files[sub] = f'https://{sub}.fandom.com/api.php'
        self.sources[title] = (sub, sub)
        self._save_sources_to_disk()
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

        if len(sources) > 0:
            abbreviated_sources = list(map(lambda source: source[:1000], sources))
            print('Found sources:', abbreviated_sources)
            prompt_template = """Given {ep_title} ({title}), the following is a discussion the relevancy of the sources to the episode.
            Current Conversation: 
            {chat_history}
            Question: {question}
            AI Response:
            """
            # prompt_template = "Out of the source snippets, which seems like the most relevant to {ep_title} ({title})?\n\n Sources:{sources}? Please respond with a number associated with the sources position in the list zero-indexed. If there is one source return 0, if there are no sources, return -1."
            context = prompt_template.format(ep_title=ep_title, title=title, sources=abbreviated_sources, chat_history="{chat_history}", question="{question}")
            prompt = PromptTemplate(template = context, input_variables=["chat_history", "question"])
            llm = ChatOpenAI(model="gpt-3.5-turbo")
            

            llm_chain = LLMChain(llm = llm, verbose = True,  prompt = prompt, memory=ConversationBufferMemory(memory_key="chat_history"))
            print(abbreviated_sources)
            source_counter = 0
            
            for s in abbreviated_sources:
                source = s
                sQuestion = f"Does this source seem relevant to the episode? If yes, return 1. If no, return 0. Source:{source}"
                answer = llm_chain.predict(question = sQuestion)
                print('Found answer:', answer)
                index = re.findall(r'\d+', answer)
                if int(index[0]) == 1:
                    return sources[source_counter]
                source_counter += 1
            return None

        # return longest plot source

        # if len(sources) > 0:
        #     print('Found sources:', sources)
        #     plot = max(sources, key=len)
        #     print('Found plot:', plot)
        #     return plot
        

        
        # TODO finally try GPT search

    # generic scraper that takes in specific site/search term format
    # returns the plot text if it finds it, otherwise returns None
    def _fetch_plot(self, site, search_term, heading_names=[]):
        search_results = pagegenerators.SearchPageGenerator(search_term, site=site, total=1)

        page = next(search_results)
        print('Scraping page: ', page.title())

        wikicode = mwparserfromhell.parse(page.text)



        # needed because mwparserfromhell just doesn't work
        sanity_check = re.search(r"\s*(?i:Plot|Summary|Main\s+story)\s*", str(wikicode))

        pattern = r"\s*(?i:Plot|Summary|Main\s+story)\s*"
        sections = wikicode.get_sections(matches=pattern, include_lead=True, include_headings=True)
        sections = list(map(lambda section: section.strip_code().strip(), sections))
       
        if len(sections) > 0 and sanity_check:
            plot = max(sections, key=lambda x: len(x))
            print('Found plot section!')
            # print(f'Found plot section: \n\"{plot}\"')
            return plot
        
    # looks for a file called sources.pickle, loads it in as a list of strings, and loops over it to populate config.family_files
    def _load_sources_from_disk(self):
        try:
            with open(SOURCES_PATH, 'rb') as f:
                self.sources = pickle.load(f)
                for show in self.sources:
                    (family, sub) = self.sources[show]
                    config.family_files[family] = f'https://{sub}.fandom.com/api.php'
                    print('Loaded source: ', family)
        except FileNotFoundError:
            print('No sources.pickle found, creating new one.')
            self.sources = {}
            self._save_sources_to_disk()


    def _save_sources_to_disk(self):
        with open(SOURCES_PATH, 'wb') as f:
            pickle.dump(self.sources, f)
            print('Saved sources to disk')


    def __del__(self):
        self._save_sources_to_disk()