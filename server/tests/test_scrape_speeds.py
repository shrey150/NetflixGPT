import requests
from bs4 import BeautifulSoup
import time

url = 'https://breakingbad.fandom.com/wiki/Ozymandias'
response = requests.get(url, timeout=5)
html_content = response.text

# Using html.parser
start_time = time.time()
soup = BeautifulSoup(html_content, 'html.parser')
end_time = time.time()
print(f"html.parser time: {end_time - start_time:.4f} seconds")

# Using lxml
start_time = time.time()
soup = BeautifulSoup(html_content, 'lxml')
end_time = time.time()
print(f"lxml time: {end_time - start_time:.4f} seconds")

# Using html5lib
start_time = time.time()
soup = BeautifulSoup(html_content, 'html5lib')
end_time = time.time()
print(f"html5lib time: {end_time - start_time:.4f} seconds")