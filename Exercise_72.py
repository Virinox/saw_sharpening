# Exercise 72
# Level 1
# written by: Vince Mao
# last modified: 2019.5.31
# Description:
# Please generate a random float value between 0 and 100 using the Python math module.
#
# Hint:
# Use the random.random() method to generate a random float in the range of [0,1].
#
# Pseudocode:
# 1. Define a function that randomly generates a float in the range of 0 and 1.
# 2. Return the float * 100 as an integer.


import random


def random_generator():
    value = random.random()
    return int(value * 100)


print random_generator()
print random_generator()
print random_generator()
