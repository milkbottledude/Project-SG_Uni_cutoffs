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

taboo = ['NA', 'Merged into Engineering', 'Computing', 'Merged into Humanities & Sciences', 'New Programme AY2024/25', '']

faculty_name = None
course_name = None
faculty_dict = {}
for i in everythang:
    print(i.text)
    if i.get('colspan') and i.text:
        if i.text not in taboo:
            faculty_name = i.text
            faculty_dict[i.text] = {}
    elif i.get('rowspan'):
        if i.text == False:
            for number in range(int(i.get('rowspan'))):
                faculty_dict[faculty_name][course_name].append('padding')
        else:
            course_name = i.text
            faculty_dict[faculty_name][i.text] = []
    else:
        if i.text:
            faculty_dict[faculty_name][course_name].append(i.text)

print(faculty_dict['School of Business'])