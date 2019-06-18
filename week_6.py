import requests
from bs4 import BeautifulSoup

zip = input('which zip? ')
url = f'https://www.wunderground.com/weather/us/pa/{zip}'
page = requests.get(url).content  # response

soup = BeautifulSoup(page, 'html.parser')
temp = soup.find('span', class_='temp')

print(temp.text)
