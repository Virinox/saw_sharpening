# Exercise 68
# Level 1
# written by: Vince Mao
# last modified: 2019.5.22
# Description:
# Please write a program using generator to print the numbers which can be divisible by 5 and 7
# between 0 and n in a comma-separated form where n is a console input.
#
# Example:
# Given the following input:
# 100
# The output should be:
# 0, 35, 70
#
# Hint:
# Use the yield method to produce the next value in the generator.
#
# Pseudocode:
# 1. Instantiate a class for the program.
# 2. Initialize an empty string in the init class.
# 3. Instantiate the method for raw input from the console.
# 4. Define a function to generate numbers divisible between 5 and 7.
# 5. Print the list of numbers.


class Prompt:
    def __init__(self):
        self.entry = ""

    def input(self):
        self.entry = raw_input("Please enter a number: ")


def generator(count):
    i = 0
    while i <= int(count):
        if i % 5 == 0 and i % 7 == 0:
            yield i
        i += 1


test = Prompt()
test.input()
solution = []
for j in generator(test.entry):
    solution.append(str(j))
print ", ".join(solution)
