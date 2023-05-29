import wikipedia
import pywikibot

site = pywikibot.Site('en', 'wikipedia') 
page = pywikibot.Page(site, 'Uno')

print(page.text)

exit()

title = 'Better Call Saul'
ep_title = 'Uno'
season_num = 1
ep_num = 1

# search Wikipedia for "{ep_title} ({title})"
def search_wiki(title, ep_title):
    res = wiki.page(f"{ep_title} ({title})")
    print('AND THE RESULT:', res)
    print(res.title, res.html())
    print(res.content)
    return
    print(res.categories)
    print(res.sections)
    print(res.summary)

search_wiki(title, ep_title)