import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.numbeo.com/cost-of-living/rankings_by_country.jsp?title=2022&displayColumn=0'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

rows = soup.find('table', {'id':"t2"}).find('tbody').find_all('tr')

countries_list = []

for row in rows: 
    dic = {}

    dic['Country'] = row.find_all('td')[1].text
    dic['Cost of living index'] = row.find_all('td')[2].text

    countries_list.append(dic)

df = pd.DataFrame(countries_list)
df.to_csv('cost_of_living.csv', index=False)

    
        