# Exercise 41
# Level 1
# written by: Vince Mao
# last modified: 2019.5.7
# Description:
# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to
# print the first half of the values in one line and the remaining values in another line.
#
# Hint:
# Use the [n1:n2] notation to slice a tuple.
#
# Pseudocode:
# 1. Define a function to generate the tuple.
# 2. Print the first 5 values on one line.
# 3. Print the remaining 5 values on the next line.


def generate_tuple():
    result = []

    for i in range(1, 11):
        result.append(i)
    return tuple(result)


test = generate_tuple()
print test[:5]
print test[5:]
