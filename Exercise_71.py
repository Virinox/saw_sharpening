# Exercise 71
# Level 2
# written by: Vince Mao
# last modified: 2019.5.27
# Description:
# Please write a binary search function that searches for an item in a sorted list.
# The function should return the index of element found in the list.
# This is essentially the same as the bisect function in Python.
#
# Hint:
# Use if/elif to deal with conditions.
#
# Pseudocode:
# 1. Define a function that takes the input for the search element and the initial list.
# 2. Sort the list.
# 3. Initialize the list length and the result.
# 4. Use a while loop to enact the binary search algorithm.
#    Make sure the upper and lower bounds are appropriate and the index has not been found.
# 5. Calculate the center as half of the sum of the upper and lower indices.
# 6. If the value at the middle index is the target, set the index to this value.
# 7. Else, if the value in the middle of the list is greater than the target,
#    assign the index to the upper index - 1. Else, set it to the lower index + 1. (Bounding purposes)
# 8. Return the result if there is a match. Otherwise the value is not in the list.


import math


def binary_search(target, series):
    series.sort()
    upper = len(series) - 1
    lower = 0
    index = -1

    while upper >= lower and index == -1:
        center = int(math.floor((upper + lower) / 2.0))
        if series[center] == target:
            index = center
        elif series[center] > target:
            upper = center - 1
        else:
            lower = center + 1

    if index == -1:
        return "Number is not in the list!"
    else:
        return index


search = [1, 4, 8, 9, 30, 35, 48]
print binary_search(1, search)
print binary_search(30, search)
print binary_search(2, search)
