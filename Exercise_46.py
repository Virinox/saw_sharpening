# Exercise 46
# Level 1
# written by: Vince Mao
# last modified: 2019.5.8
# Description:
# Write a program which can map() and filter() to create a list with elements
# that are squares of the even numbers in the list [1,2,3,4,5,6,7,8,9,10].
#
# Hint:
# Use the map() method to generate a list.
# Use the filter() method to filter elements of a list.
# Use lambda to define anonymous functions.
#
# Pseudocode:
# 1. Define a function to generate the list.
# 2. Generate a new list by using the filter() method to create a list of the even numbers in the initial list.
# 3. Use the map() method to square values from the new list using a lambda function.
# 4. Return the resulting list


def filter_squares():
    test = []

    for i in range(1, 11):
        test.append(i)
    even = list(filter(lambda x: (x % 2 == 0), test))
    result = list(map(lambda x: (x ** 2), even))
    return result


print filter_squares()
