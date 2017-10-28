# practicepython.py
#
# Solution by: Lukasz Sikora
# Date: 28th October, 2017
#
#
# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.
#
# Extra:
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
import random

def gen_pass(pass_size):
    pass_pool = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+"
    str = random.sample(pass_pool,pass_size)
    return "".join(str)


print("=== PASSWORD GENERATOR ====")
try:
    password_size = int(input("How many characters should password contain? "))
except ValueError:
    print("Please only use numbers")

print(gen_pass(password_size))




