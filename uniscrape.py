import csv

import pandas as pd
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
years = []
increment = 0
everythang.pop(0)
for thang in everythang:
    if increment == 17:
        break
    years.append(thang.text)
    increment += 1
    everythang.pop(0)

data = {
    'years': years
}

df = pd.DataFrame(data)

track = 1
without_faculty = []
faculty_name = None
faculty_dict = {}
for i in everythang:
    if track == 53:
        track = 1
    if 'of' not in i.text:
        without_faculty.append(i.text)
        print(track, i.text)
        track += 1
        faculty_dict[faculty_name].append(i.text)
    else:
        faculty_name = i.text
        faculty_dict[i.text] = []


