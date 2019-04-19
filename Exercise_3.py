# Exercise 3
# Level 1
# written by: Vince Mao
# last modified: 2019.4.18
# Description:
# With a given integer number n, write a program to generate a dictionary that contains (i, i*i)
# such that there is an integer number between 1 and n (both included). The program should return the dictionary.
# Example: Suppose the following input is supplied to the program:
# 8
# The result should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
#
# Hints:
# The input should be assumed to be a console input.
# Consider using the dict() method.
#
# Pseudocode:
# 1. Pass the value in from an external variable
# 2. Initialize an empty dictionary
# 3. Loop over the range from 1 to n + 1
# 4. Add the iterable value as the key and the square as the value to the dictionary
# 5. Return the dictionary


def dict_gen(value):
    result = {}
    for i in range(1, value + 1):
        result[i] = i * i

    return result


entry = raw_input("Enter a number: ")
print dict_gen(int(entry))
