# Exercise 82
# Level 1
# written by: Vince Mao
# last modified: 2019.6.6
# Description:
# Please write a program to shuffle and print the list [3, 6, 7, 8].
#
# Hint:
# Use the shuffle() method from the random module to shuffle a list.
#
# Pseudocode:
# 1. Import shuffle from the random module.
# 2. Initialize the list [3, 6, 7, 8].
# 3. Use the shuffle() module to shuffle the list.

from random import shuffle


test = [3, 6, 7, 8]
shuffle(test)
print test
