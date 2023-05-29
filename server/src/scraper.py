import pywikibot
from pywikibot import pagegenerators 
from langchain.chat_models import ChatOpenAI
import mwparserfromhell

from dotenv import load_dotenv
load_dotenv()

title = 'Breaking Bad'
ep_title = 'Remedial Chaos Theory'
season_num = 1
ep_num = 1

site = pywikibot.Site("en", "wikipedia") # TODO: add support for Fandom

search_term = f"{ep_title} ({title})"
search_results = pagegenerators.SearchPageGenerator(search_term, site=site, total=1)

page = next(search_results)
wikicode = mwparserfromhell.parse(page.text)

plot_section = None
for section in wikicode.get_sections():
    heading = section.filter_headings() # Get the first heading in the section
    if len(heading) == 0:
        continue

    heading_text = heading[0].title.strip() if heading else ""  # Get the text of the heading, or an empty string if there is no heading

    if heading_text == "Plot":
        plot_section = section
        break

if plot_section is not None:
    plot_text = plot_section.strip_code().strip()
    print(plot_text)