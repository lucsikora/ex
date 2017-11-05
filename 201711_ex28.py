# practicepython.py
#
# Solution by: Lukasz Sikora
# Date: 5th November, 2017
#
#
# Implement a function that takes as input three variables, and returns the largest of the three. Do this without
# using the Python max() function!
#
# The goal of this exercise is to think about some internals that Python normally takes care of for us. All you
# need is some variables and if statements!

def input_nums():
    nums = input("Give me 3 numbers separeted by space: ").split(' ')
    return nums

def show_max(nums):
    print(nums)
    max_num = nums[0]
    if max_num < nums[1]:
        max_num = nums[1]
    if max_num < nums[2]:
        max_num = nums[2]
    return max_num


if __name__ == "__main__":
    print(show_max(input_nums()))