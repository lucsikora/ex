# practicepython.py
#
# Solution by: Lukasz Sikora
# Date: 30th October, 2017
#
#
# Use the BeautifulSoup and requests Python packages to print out a list
# of all the article titles on the New York Times homepage.

import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.textpip

soup = BeautifulSoup(r_html)
title = soup.find('class', 'story-heading').string
print(title)
# print(r_html)