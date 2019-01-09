#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.mirandalambert.com/tour/")

soup = BeautifulSoup(r.content, features="html.parser")

dates = soup.find_all("a", "date")
cities = soup.find_all("a", "city")

print('')

for i in range(len(dates)):
    print(f'{dates[i].string:20} {cities[i].string}')


# Output:
#
# June 21, 2019        Chicago, IL
# July 24, 2019        Cheyenne, WY
# August 16, 2019      Calgary, AB
# August 8-11, 2019    Oro-Medonte, ON
