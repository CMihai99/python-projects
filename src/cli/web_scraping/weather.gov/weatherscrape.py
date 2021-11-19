# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: November 19th, 2021

import requests
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.09927000000005&lon=-118.33806999999996#.XIRJ81NKgUE')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')

items = week.find_all(class_='tombstone-container')

print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())

period_names = [item.find(class_='period-name').get_text() for item in items]
short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]
print(period_names)

weather_info = pd.DataFrame(
    {
        'period': period_names,
        'short_descriptions': short_descriptions,
        'temperatures': temperatures,
    })

print(weather_info)

# Convert To CSV
weather_info.to_csv('weather.csv')
