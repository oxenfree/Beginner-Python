import requests
from bs4 import BeautifulSoup

zip_code = input('which zip? ')
url = f'https://www.wunderground.com/weather/us/pa/{zip_code}'
page = requests.get(url).content  # response

soup = BeautifulSoup(page, 'html.parser')
temp = soup.find('span', class_='temp')

print(temp.text)
