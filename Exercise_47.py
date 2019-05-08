# Exercise 47
# Level 1
# written by: Vince Mao
# last modified: 2019.5.8
# Description:
# Write a program that uses filter() to make a list containing elements with
# even numbers between 1 and 20 (both included).
#
# Hint:
# Use the filter() method to filter elements of a list.
# Use lambda to define anonymous functions.
#
# Pseudocode:
# 1. Define a function to generate the list.
# 2. Generate a new list by using the filter() method to create a list of the even numbers in the initial list.
# 3. Return the list.


def filter_even():
    test = []

    for i in range(1, 21):
        test.append(i)
    result = list(filter(lambda x: (x % 2 == 0), test))
    return result


print filter_even()
