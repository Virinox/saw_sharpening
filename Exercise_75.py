# Exercise 75
# Level 1
# written by: Vince Mao
# last modified: 2019.5.31
# Description:
# Please write a program to output a random number, which is divisible by 5 and 7,
# between 0 and 200 inclusive using the random module and list comprehension.
#
# Hint:
# Use the random.choice() method to generate a random element from a list.
#
# Pseudocode:
# 1. Define a function that generates a list of numbers including 0 and 200 that are divisible by 5 and 7.
# 2. Return the randomly chosen number from the list.


import random


def random_generator():
    choices = []
    for i in range(201):
        if i % 5 == 0 and i % 7 == 0:
            choices.append(i)
    return random.choice(choices)


print random_generator()
print random_generator()
print random_generator()
