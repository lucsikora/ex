# practicepython.py
#
# Solution by: Lukasz Sikora
# Date: 3rd November, 2017
#
#
# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and
# print out the results to the screen. I have a .txt file for you, if you want to use it!
#
# Extra:
#
#     Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file, and
#  count how many of each “category” of each image there are. This text file is actually a list of files corresponding
#  to the SUN database scene recognition database, and lists the file directory hierarchy for the images.
# Once you take a look at the first line or two of the file, it will be clear which part represents the scene category.
# To do this, you’re going to have to remember a bit about string parsing in Python 3. I talked a little bit
# about it in this post.


def specify_name():
    return raw_input("Please specify name of file to be open: ")


def readfile(filename="names_ex22"):
    with open(filename, 'r') as open_file:
        licznik = {'Darth': 0, 'Luke': 0, 'Lea': 0}
        line = open_file.readline().rstrip()
        while line:
            if line == "Darth":
                licznik['Darth'] += 1
            elif line == "Luke":
                licznik['Luke'] += 1
            elif line == "Lea":
                licznik['Lea'] += 1
            line = open_file.readline().rstrip()
        print("Darth:", licznik['Darth'], "Luke:", licznik['Luke'], "Lea: ", licznik['Lea'])


if __name__ == "__main__":
    readfile(specify_name())
