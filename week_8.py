import requests
from bs4 import BeautifulSoup
import csv

url = f'https://www.wunderground.com/hourly/us/pa/pittsburgh/15262?cm_ven=localwx_hour'
response = requests.get(url).content  # response
soup = BeautifulSoup(response, 'html.parser')
table = soup.find('table', id='hourly-forecast-table')
table_body = table.find('tbody')
rows = table_body.find_all('tr')

count = 0
with open('pittsburgh_conditions.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['hour', 'condition'])
    for row in rows:
        cols = row.find_all('td')
        conditions_td = cols[1]
        condition = conditions_td.find('span', class_='show-for-medium')
        if count == 0:
            count += 1
        writer.writerow([cols[0].text.strip(), condition.text])
