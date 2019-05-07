# Exercise 39
# Level 1
# written by: Vince Mao
# last modified: 2019.5.7
# Description:
# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included)
# and the values are squares of the keys. The function should print the keys only.
#
# Hint:
# Use dict[key]=value to add an entry into a dictionary.
# Use the ** operator to calculate the power of a number.
# Use the range method in the for loop.
# Use keys() to iterate through keys in a dictionary.
# Use item() to get key/value pairs.
#
# Pseudocode:
# 1. Define a function that loops in the range of 1 to 21.
# 2. Add a dictionary entry for each key value and assign the square of the value.
# 3. Return the keys for the dictionary.


def square_values():
    result = {}

    for i in range(1, 21):
        result[i] = i ** 2
    for (keys, values) in result.items():
        print keys
    return result.keys()


print square_values()
