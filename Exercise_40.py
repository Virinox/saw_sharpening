# Exercise 40
# Level 1
# written by: Vince Mao
# last modified: 2019.5.7
# Description:
# Define a function which can generate and print a tuple where the values are squares of numbers
# between 1 and 20 (both included).
#
# Hint:
# Use the ** operator to calculate the power of a number.
# Use the range() method for loops.
# Use the list.append() method to add values to a list.
# Use the tuple() method to convert a list to a tuple.
#
# Pseudocode:
# 1. Define a function that loops in the range of 1 to 21.
# 2. Append the result to an array.
# 3. Return the tuple of the array.


def square_tuple():
    result = []

    for i in range(1, 21):
        result.append(i ** 2)
    return tuple(result)


print square_tuple()
