# Exercise 42
# Level 1
# written by: Vince Mao
# last modified: 2019.5.7
# Description:
# Write a program to generate and print a tuple that contains the even values in the given tuple (1,2,3,4,5,6,7,8,9,10).
#
# Hint:
# Use a for loop
# Use the tuple() method to generate a tuple from a list.
#
# Pseudocode:
# 1. Define a function to generate the tuple.
# 2. Create another tuple by iterating through the values of given tuple and adding the even numbers.
# 3. Print the resulting tuple.


def generate_tuple():
    result = []
    generate = []

    for i in range(1, 11):
        generate.append(i)
    for j in range(len(generate)):
        if not generate[j] % 2:
            result.append(generate[j])
    return tuple(result)


print generate_tuple()
