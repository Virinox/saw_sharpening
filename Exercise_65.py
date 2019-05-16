# Exercise 65
# Level 1
# written by: Vince Mao
# last modified: 2019.5.15
# Description:
# The Fibonacci Sequence is computed based on the following formula:
#
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
#
# Please write a program to compute the value of f(n) with a given n input via console.
#
# Example:
# Given the following input:
# 7
# The output should be:
# 13
#
# Hint:
# The data should be assumed to be a console input.
# Use recursion.
#
# Pseudocode:
# 1. Instantiate a class for the program.
# 2. Initialize an empty string in the init class.
# 3. Instantiate the method for raw input from the console.
# 4. Instantiate the function for going through the string and calculate the given equation.
# 5. Call the recursive function based on input.


class Prompt:
    def __init__(self):
        self.entry = ""

    def input(self):
        self.entry = raw_input("Please enter a number: ")


def fibonacci(count):
    if str(count).isdigit():
        current = int(count)
        if current == 0:
            return 0
        if current == 1:
            return 1
        else:
            return fibonacci(current - 1) + fibonacci(current - 2)
    else:
        return "Not a number!"


test = Prompt()
test.input()
print fibonacci(test.entry)
