import pywikibot
import uvicorn
from app.server import app

from dotenv import load_dotenv
from constants import *
from app.scraper import Scraper
from app.models import TitleInfo

load_dotenv(DOTENV_PATH)

def main():
    scraper = Scraper()

    community_remedial_chaos_theory = TitleInfo(
        title="Community",
        ep_title="Remedial Chaos Theory",
        season_num=3,
        ep_num=4,
        summary=None,
    )

    # print(scraper._fetch_plot(pywikibot.Site("succession", "succession"), "Austerlitz"))
    # print(scraper._fetch_plot(pywikibot.Site("breakingbad", "breakingbad"), "Ozymandias"))
    print(scraper._fetch_plot(pywikibot.Site("community-sitcom", "community-sitcom"), "Remedial Chaos Theory", community_remedial_chaos_theory))

    # print the previous 3 lines using pywikibot.Site("en", "wikipedia")
    # print(scraper._fetch_plot(pywikibot.Site("en", "wikipedia"), "Austerlitz (Succession)"))
    # print(scraper._fetch_plot(pywikibot.Site("en", "wikipedia"), "Ozymandias (Breaking Bad)"))
    print(scraper._fetch_plot(pywikibot.Site("en", "wikipedia"), "Remedial Chaos Theory (Community)"))

    print(scraper.get_fandom_sub("community"))

if __name__ == '__main__':
    main()