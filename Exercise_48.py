# Exercise 48
# Level 1
# written by: Vince Mao
# last modified: 2019.5.8
# Description:
# Write a program which uses map() to create a list that contains
# elements which are squares of numbers between 1 and 20 (both included).
#
# Hint:
# Use the map() method to map elements of a list.
# Use lambda to define anonymous functions.
#
# Pseudocode:
# 1. Define a function to generate the list.
# 2. Generate a new list by using the map() method to create a list of the squared numbers in the initial list.
# 3. Return the list.


def squared_map():
    test = []

    for i in range(1, 21):
        test.append(i)
    result = list(map(lambda x: x ** 2, test))
    return result


print squared_map()
