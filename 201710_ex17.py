# practicepython.py
#
# Solution by: Lukasz Sikora
# Date: 1st November, 2017
#
#
# Use the BeautifulSoup and requests Python packages to print out a list
# of all the article titles on the New York Times homepage.

import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)

# r_html = r.text
# soup = BeautifulSoup(r_html, "html.parser")
# for div in soup.find_all("h2", {"class": "story-heading"}):
#     print(div.find("a").string)

soup = BeautifulSoup(r.text, "html.parser")
headings = soup.findAll("h2", {"class": "story-heading"})

for heading in headings:
    if heading.findAll("a"):
        print(heading.a.text.strip())
    else:
        print(heading.text)