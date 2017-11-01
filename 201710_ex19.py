# practicepython.py
#
# Solution by: Lukasz Sikora
# Date: 1st November, 2017
#
#
# Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article
# on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
#
# The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen
#  so that you can read the full article without having to click any buttons.
#
# (Hint: The post here describes in detail how to use the BeautifulSoup and requests libraries through the
# solution of the exercise posted here.)
#
# This will just print the full text of the article to the screen. It will not make it easy to read, so next
#  exercise we will learn how to write this text to a .txt file.

import requests
# from __builtin__ import raw_input
from bs4 import BeautifulSoup

def getportions(soup):
    heading = soup.find("div", {"class": "dek"})
    if heading:
        yield heading.text

    for p in soup.find_all("p", {"class": ""}):
        yield p.text


def parsepage(address):
    page = requests.get(address)
    soup = BeautifulSoup(page.text, "html.parser")

    for s in getportions(soup):
        print("\n%s" % s.encode("utf-8"))
        input("\nPress enter to continue ")

        # raw_input("\nPress enter to continue  ")
    print("End of article")


if __name__ == "__main__":
    parsepage("http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture")
