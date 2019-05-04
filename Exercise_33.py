# Exercise 32
# Level 1
# written by: Vince Mao
# last modified: 2019.5.3
# Description:
# Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included)
# and the values are squares of the keys.
#
# Hint:
# Use dict[key]=value to add an entry into a dictionary.
# Use the ** operator to calculate the power of a number.
# Use the range method in the for loop.
#
# Pseudocode:
# 1. Define a function that loops in the range of 1 to 21.
# 2. Add a dictionary entry for each key value and assign the square of the value.
# 3. Return the keys and their square values.


def squares():
    result = {}

    for i in range(1, 21):
        result[i] = i ** 2
    return result


print squares()
