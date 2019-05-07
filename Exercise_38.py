# Exercise 38
# Level 1
# written by: Vince Mao
# last modified: 2019.5.7
# Description:
# Define a function which can generate and print a list where the values are
# the square of numbers between 1 and 20 (both included). Print the last 5 elements in the list.
#
# Hint:
# Use the ** operator to calculate the power of a number.
# Use the range() method for loops.
# Use the list.append() method to add values to a list.
# Use [n1:n2] to slice a list.
#
# Pseudocode:
# 1. Define a function that loops in the range of 1 to 21.
# 2. Append the result to an array.
# 3. Return the slice of the array.


def square_slice():
    result = []

    for i in range(1, 21):
        result.append(i ** 2)
    return result[15:]


print square_slice()
