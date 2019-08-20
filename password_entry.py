""" Jack Smith """
import random

finished = False
min_length = random.randint(5, 20)
while not finished:
    password = input("Please enter your {} character minimum password password: ".format(min_length))
    if len(password) < min_length:
        print("Password must be at least {} characters long".format(min_length))
    else:
        finished = True

for i in password:
    print("*", end=" ")

print("\nYour password is valid")
