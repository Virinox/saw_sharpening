# Exercise 45
# Level 1
# written by: Vince Mao
# last modified: 2019.5.8
# Description:
# Write a program using the map() method to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
#
# Hint:
# Use the map() method to map value manipulation for elements in a list.
# Use lambda to define an anonymous functions.
#
# Pseudocode:
# 1. Define a function to generate the list.
# 2. Generate a new list by using the map() method to square values from the initial list using a lambda function.
# 3. Return the resulting list


def map_squares():
    test = []

    for i in range(1, 11):
        test.append(i)

    result = list(map(lambda x: (x ** 2), test))
    return result


print map_squares()
