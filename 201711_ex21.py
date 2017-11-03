# practicepython.py
#
# Solution by: Lukasz Sikora
# Date: 3rd November, 2017
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


def specify_file():
    filename = raw_input("Please specify file name: ")
    return filename


def save_to_file(file_content, filename):
    with open(filename, 'a') as open_file:
        open_file.write(file_content.encode('utf-8') + "\n")


def readpage():
    url = 'https://www.nytimes.com/'
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")
    headings = soup.findAll("h2", {"class": "story-heading"})
    final_file_name = specify_file()

    for heading in headings:
        if heading.findAll("a"):
            save_to_file(heading.a.text.strip(), final_file_name)
            # print(heading.a.text.strip())
        else:
            save_to_file(heading.text, final_file_name)
            # print(heading.text)

readpage()
