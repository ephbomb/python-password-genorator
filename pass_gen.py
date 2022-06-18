# A program that genorates random passwords with as many characters as you choose.

import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+"

while 1:
    password_length = int(input(("What length would you like your password to be : ")))
    password_count = int(input("How many passwords do you want to generate? : "))
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_length):
            password_char = random.choice(chars)
            password      = password + password_char
        print("Here is your password : ", password)
        