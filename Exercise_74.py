# Exercise 74
# Level 1
# written by: Vince Mao
# last modified: 2019.5.31
# Description:
# Please write a program to output a random even number between 0 and 10 inclusive
# using the random module and list comprehension.
#
# Hint:
# Use the random.choice() method to generate a random element from a list.
#
# Pseudocode:
# 1. Define a function that generates a list of even numbers including 0 and 10.
# 2. Return the randomly chosen number from the list.


import random


def random_generator():
    choices = []
    for i in range(11):
        if i % 2 == 0:
            choices.append(i)
    return random.choice(choices)


print random_generator()
print random_generator()
print random_generator()

print random.choice([i for i in range(11) if i % 2 == 0])
