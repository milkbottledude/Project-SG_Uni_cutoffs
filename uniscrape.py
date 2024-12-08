import csv
import requests
from bs4 import BeautifulSoup

url = 'https://docs.google.com/spreadsheets/d/1MPEDZpw26TjN7dTsQzsbnXHZa47og0qSrdHrlT7nLKc/pubhtml#'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
content = soup.find_all('tbody')
# all = content.find_all('td')
content.pop(0)
test_w_nus = content[0]
everythang = test_w_nus.find_all('td')
