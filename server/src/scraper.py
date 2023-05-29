import pywikibot
from pywikibot import pagegenerators, config
from langchain.chat_models import ChatOpenAI
import mwparserfromhell

title = 'The Recruit'
ep_title = 'I.N.A.S.I.A.L.'
season_num = 1
ep_num = 1

def fetch_plot(site, title, ep_title):
    # TODO: consider using SerpAPI to search for the fandom page instead of MediaWiki's search engine
    search_term = f"{ep_title} ({title} TV Series)"
    search_results = pagegenerators.SearchPageGenerator(search_term, site=site, total=1)

    page = next(search_results)
    print('Scraping page: ', page.title())

    wikicode = mwparserfromhell.parse(page.text)
    
    for section in wikicode.get_sections():
        heading = section.filter_headings()

        if heading and len(heading) > 0:
            heading_text = heading[0].title.strip() if heading else ""
            print(heading_text)

            # TODO: consider using LLM to pick the heading that best fits plot summary
            # OR pass the entire section into LLM to find content best matching plot summary
            if heading_text == "Plot":
                plot_text = section.strip_code().strip()
                return plot_text
            
def fetch_wikipedia(title, ep_title):
    site = pywikibot.Site("en", "wikipedia")
    return fetch_plot(site, title, ep_title)

def fetch_fandom(title, ep_title, sub):
    site = pywikibot.Site("en", sub)
    return fetch_plot(site, title, ep_title)

if __name__ == "__main__":
    # TODO: add families dynamically based on the URL of the fandom page
    config.family_files['netflix'] = 'https://netflix.fandom.com/api.php'
    config.family_files['fandom'] = 'https://fandom.com/api.php'

    wiki_res = fetch_wikipedia(title, ep_title)
    if wiki_res is not None:
        print(wiki_res)
        exit()

    print('No Wikipedia result, fetching from Fandom')

    fandom_res = fetch_fandom(title, ep_title, "netflix")
    if fandom_res is not None:
        print(fandom_res)
        exit()

    # TODO: use the first search engine link & use LLM to scrape the plot summary