# Exercise 4
# Level 1
# written by: Vince Mao
# last modified: 2019.4.20
# Description:
# Write a program which accepts a sequence of comma-separated numbers from console and generate a
# list and a tuple which contains every number.
# Example: Suppose the following input is supplied to the program:
# 34, 67, 55, 33, 12, 98
# The result should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
#
# Hints:
# The input should be assumed to be a console input.
# The tuple() method can convert a list to a tuple.
#
# Pseudocode:
# 1. Prompt entry of comma-separated numbers
# 2. Take the string result and convert into a list and a tuple
# 3. Return the list and tuple versions of the data


def list_to_tuple(text):
    result = text.split(',')
    for i in range(len(result)):
        if not result[i].isdigit():
            return "Integers only please!"
    solution = list(result), tuple(result)
    return solution


entry = raw_input("Please enter numbers separated by a comma: ")
print list_to_tuple(entry)
