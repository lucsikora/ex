# practicepython.py
#
# Solution by: Lukasz Sikora
# Date: 29th October, 2017
#
#
# Use the BeautifulSoup and requests Python packages to print out a list
# of all the article titles on the New York Times homepage.

import requests
url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.textpip

print(r_html)