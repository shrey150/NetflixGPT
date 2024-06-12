import pywikibot
import requests
from pywikibot import pagegenerators, config
from bs4 import BeautifulSoup

custom_sub = "breakingbad"
search_term = "Sabrosito"

# Set up the custom site configuration
config.family_files[custom_sub] = f'https://{custom_sub}.fandom.com/api.php'
site = pywikibot.Site(custom_sub, custom_sub)

# Search for the page
search_results = pagegenerators.SearchPageGenerator(search_term, site=site, total=1, namespaces=[0])

print(search_results)

# Get the first page from the search results
page = next(search_results)
print('Scraping page: ', page.title())

url = f'https://{custom_sub}.fandom.com/wiki/{page.title().replace(" ", "_")}'

response = requests.get(url, timeout=5)

if response.status_code != 200:
    print(f"Failed to retrieve data: {response.status_code}")
else:
    soup = BeautifulSoup(response.text, 'html5lib')
    # Using CSS selectors to get all p tags that are children of mw-parser-output
    paragraphs = soup.select('.mw-parser-output > p')
    text_content = ' '.join(p.get_text() for p in paragraphs)
    print(text_content)