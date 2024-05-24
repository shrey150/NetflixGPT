import requests
from bs4 import BeautifulSoup

def search_community(query):
    base_url = "https://community.fandom.com/wiki/Special:SearchCommunity"
    params = {
        'query': query
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code != 200:
        print(f"Failed to retrieve data: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    results = []

    # Assuming search results are within specific HTML elements; adjust selectors as needed
    for item in soup.select('.unified-search__result__title'):
        title = item.get_text()
        link = item['href']
        results.append({'title': title, 'link': link})

    return results

def main():
    query = "the end of the fucking world"  # Your search query
    results = search_community(query)

    for result in results:
        print(f"Title: {result['title']}\nLink: {result['link']}\n")

if __name__ == "__main__":
    main()