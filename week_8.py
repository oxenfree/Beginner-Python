import requests
from bs4 import BeautifulSoup
import csv

url = f'https://www.wunderground.com/hourly/us/pa/pittsburgh/15262?cm_ven=localwx_hour'
response = requests.get(url).content  # response

soup = BeautifulSoup(response, 'html.parser')
table = soup.find('table', id='hourly-forecast-table')
table_body = table.find('tbody')
trs_list = table_body.find_all('tr')  # list of trs (rows)

with open('pittsburgh_conditions_test.csv', 'w') as csv_file:
    row_writer = csv.writer(csv_file)
    # write once at the top
    row_writer.writerow(['hour', 'condition', 'cloud_cover'])
    for row in trs_list:  # repeat for every row in rows
        tds_list = row.find_all('td')  # list of tds (cells)
        time_text = tds_list[0].text.strip()  # 1:00 pm
        conditions_td = tds_list[1]  # sunny
        # beautiful soup syntax below
        cloud_cover = tds_list[6]
        cloud_text = cloud_cover.find('span').text.strip()
        condition = conditions_td.find(
            'span', class_='show-for-medium').text.strip()
        row_writer.writerow([time_text, condition, cloud_text])
