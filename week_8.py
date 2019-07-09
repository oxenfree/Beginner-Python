import requests
from bs4 import BeautifulSoup
import csv

url = f'https://www.wunderground.com/hourly/us/pa/pittsburgh/15262?cm_ven=localwx_hour'
# use requests to 'get' the page
response = requests.get(url)  # the response
response_html = response.content

# feed the html in BeautifulSoup because parsing html is hard
# and they've already figured it out
soup = BeautifulSoup(response_html, 'html.parser')

# 'find' the table we want
table = soup.find('table', id='hourly-forecast-table')

# 'find' the body of the table
table_body = table.find('tbody')

# 'find_all' the rows (trs) and make them into a list
trs_list = table_body.find_all('tr')  # list of trs (rows)

# make a file and set the variable in the weird backwards syntax
with open('pittsburgh_conditions_test.csv', 'w') as csv_file:

    # get the writer from the csv library
    row_writer = csv.writer(csv_file)

    # write the next line once at the top of our csv file
    row_writer.writerow(['hour', 'condition', 'cloud_cover'])

    # trs_list is just a list. let's iterate through it
    for row in trs_list:
        # 'find_all' the tds and put them in a list
        tds_list = row.find_all('td')

        # pull the first [0]th td and strip the text
        time_text = tds_list[0].text.strip()  # 1:00 pm

        # pull the second [1]th td, this is a jumble of html
        conditions_td = tds_list[1]

        # 'find' the first span from the jumble
        condition_span = conditions_td.find('span', class_='show-for-medium')
        # pull the text from that span and strip off the cruft
        condition_text = condition_span.text.strip()

        # let's do the cloud cover percentage!
        # beautiful soup syntax below, we've seen it before
        cloud_cover_html = tds_list[6]  # this is a jumble of html
        cloud_span = cloud_cover_html.find('span')  # a span in that jumble
        cloud_text = cloud_span.text.strip()  # the text we want

        # now we use our csv writer to write out all the variables
        # we gathered
        row_writer.writerow([time_text, condition_text, cloud_text])

# fin!
