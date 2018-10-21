import requests
from bs4 import BeautifulSoup

url = 'https://www.joe.co.uk/life/a-definitive-ranking-of-every-swear-word-from-worst-to-best-122544'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

text = soup.find_all('p')

for word in soup.find_all('strong'):
    print(word.get_text())