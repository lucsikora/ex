# practicepython.py
#
# Solution by: Lukasz Sikora
# Date: 4th November, 2017
#
#
# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
# One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy
# numbers up to 1000.
#
# (If you forgot, prime numbers are numbers that can’t be divided by any other number. And yes, happy numbers
# are a real thing in mathematics - you can look it up on Wikipedia. The explanation is easier with an example,
# which I will describe below.)


def main():
    with open('ex23_num1', 'r') as x:
        collection_one = [int(line.strip()) for line in x]
    with open('ex23_num2', 'r') as x:
        collection_two = [int(line.strip()) for line in x]

    overlap = [x for x in collection_one if x in collection_two]
    print(overlap)


if __name__ == "__main__":
    main()