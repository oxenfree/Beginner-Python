import os
import requests
# from bs4 import BeautifulSoup

url = 'https://www.wunderground.com/weather/us/pa/pittsburgh/15262'
page = requests.get(url)

# soup = BeautifulSoup(page, 'html.parser')
# temp = soup.find('span', class_='temp')

print(page)