import requests
from bs4 import BeautifulSoup
import json

# Carica il valore precedente dal file JSON (se esiste)
try:
    with open('previous_value.json', 'r') as f:
        previous_value = json.load(f)['value']
except FileNotFoundError:
    previous_value = None

url = 'https://ipogo.app'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

element = soup.select_one('body > div.page-header.header-filter > div > div > div > div > small:nth-child(1)')

