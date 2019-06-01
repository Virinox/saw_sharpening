# Exercise 72
# Level 1
# written by: Vince Mao
# last modified: 2019.5.31
# Description:
# Please generate a random float value between 5 and 95 using the Python math module.
#
# Hint:
# Use the random.randint() method to generate a random float in the range of [a, b].
#
# Pseudocode:
# 1. Define a function that randomly generates an integer in the range of 5 and 95.
# 2. Return the integer.


import random


def random_generator():
    value = random.randint(5, 95)
    return value


print random_generator()
print random_generator()
print random_generator()
