# Need to import the payload from some CSV file
# info =  {
#     "title": "The Office",
#     "ep_title": "The Dundies",
#     "season_num": 2,
#     "ep_num": 1,
# }
import sys
from os import path
try:
    from app.scraper import Scraper
    from app.db import Database
except ModuleNotFoundError:
    sys.path.append(path.join(path.dirname(__file__), '..'))
    from app.scraper import Scraper
    from app.db import Database
from suits_episodes import suits_db
from dotenv import load_dotenv
from app.models import TitleInfo, PageInfo


load_dotenv('../.env')

db = Database()
scraper = Scraper()
for e in suits_db:
    if not db.has(e):
            #Convert dictionary e to TitleInfo object?
            title_e = TitleInfo(**e)
            print(e, type(e))
            summary = scraper.fetch(title_e)  
            print('summary', summary)
            db.add(summary, e)




