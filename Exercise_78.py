# Exercise 78
# Level 1
# written by: Vince Mao
# last modified: 2019.6.3
# Description:
# Please write a program to randomly generate a list with 5 numbers,
# which are divisible by 5 and 7 , between 1 and 1000 inclusive.
#
# Hint:
# Use the random.sample() method to generate a list of random values.
#
# Pseudocode:
# 1. Print a randomly generated list of 5  numbers between 1 and 1000
#    using the random.sample() method, if statements, and range.


import random

print random.sample([i for i in range(1001) if i % 5 == 0 and i % 7 == 0], 5)
