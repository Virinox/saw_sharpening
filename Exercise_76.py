# Exercise 76
# Level 1
# written by: Vince Mao
# last modified: 2019.6.3
# Description:
# Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.
#
# Hint:
# Use the random.sample() method to generate a list of random values.
#
# Pseudocode:
# 1. Print a randomly generated list of 5 numbers including 100 and 200  using the random.sample() method and xrange.


import random

print random.sample(xrange(100, 201), 5)
