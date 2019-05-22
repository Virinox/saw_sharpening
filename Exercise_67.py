# Exercise 67
# Level 1
# written by: Vince Mao
# last modified: 2019.5.22
# Description:
# Please write a program using a generator to print the even numbers between 1 and n
# in a comma-separated form where n is a console input.
#
# Example:
# Given the following input:
# 10
# The output should be:
# 2, 4, 6, 8, 10
#
# Hint:
# Use the yield method to produce the next value in the generator.
#
# Pseudocode:
# 1. Instantiate a class for the program.
# 2. Initialize an empty string in the init class.
# 3. Instantiate the method for raw input from the console.
# 4. Define a function to generate even numbers.
# 5. Print the list of even numbers.


class Prompt:
    def __init__(self):
        self.entry = ""

    def input(self):
        self.entry = raw_input("Please enter a number: ")


def generator(count):
    i = 1
    while i <= int(count):
        if i % 2 == 0:
            yield i
        i += 1


test = Prompt()
test.input()
solution = []
for j in generator(test.entry):
    solution.append(str(j))
print ", ".join(solution)
