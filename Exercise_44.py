# Exercise 44
# Level 1
# written by: Vince Mao
# last modified: 2019.5.7
# Description:
# Write a program that can filter even numbers in a list by using a filter function.
# The list is: [1,2,3,4,5,6,7,8,9,10].
#
# Hint:
# Use the filter() method to filter some elements in a list.
# Use lambda to define an anonymous functions.
#
# Pseudocode:
# 1. Define a function to generate the list.
# 2. Generate a new list by filtering out all even values from the initial list using a lambda function.
# 3. Return the resulting list


def filter_even():
    test = []

    for i in range(1, 11):
        test.append(i)

    result = list(filter(lambda x: (x % 2 == 0), test))
    return result


print filter_even()
