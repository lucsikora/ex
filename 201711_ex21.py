# practicepython.py
#
# Solution by: Lukasz Sikora
# Date: 2nd November, 2017
#
#
# Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to
# play with some different code, use the code from the solution), and instead of printing the results to
# a screen, write the results to a txt file. In your code, just make up a name for the file you are saving to.
#
# Extras:
#
#     Ask the user to specify the name of the output file that will be saved.

import requests
from bs4 import BeautifulSoup


# def specify_file():
#     filename = input("Please specify file name: ")
#     return filename


def save_to_file(file_content):
    # filename = specify_file()
    with open('sample.txt', 'w') as open_file:
        open_file.write(file_content)


def readpage():
    url = 'https://www.nytimes.com/'
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")
    headings = soup.findAll("h2", {"class": "story-heading"})

    for heading in headings:
        if heading.findAll("a"):
            save_to_file(heading.a.text.strip())
            # print(heading.a.text.strip())
        else:
            save_to_file(heading.text)
            # print(heading.text)

readpage()
