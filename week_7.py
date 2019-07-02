import requests
from bs4 import BeautifulSoup
import re

again = True
temps = {}
while again:
    state = input('which state? ')
    zip_code = input('which zip? ')
    url = f'https://www.wunderground.com/weather/us/{state}/{zip_code}'
    page = requests.get(url).content  # response
    soup = BeautifulSoup(page, 'html.parser')
    temp = soup.find('span', class_='temp')
    temps[zip_code] = temp.text.strip()
    go_again = input('go again? ')
    if 'y' in go_again:
        again = True
    else:
        again = False

print(temps)
