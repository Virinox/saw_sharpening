# Exercise 66
# Level 1
# written by: Vince Mao
# last modified: 2019.5.22
# Description:
# The Fibonacci Sequence is computed based on the following formula:
#
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
#
# Please write a program using list comprehension to print the Fibonacci Sequence
# in a comma-separated form given n input by console.
#
# Example:
# Given the following input:
# 7
# The output should be:
# 0, 1, 1, 2, 3, 5, 8, 13
#
# Hint:
# Use recursion.
# Use list comprehension to generate a list from an existing list.
# Use string.join() to join a list of strings.
#
# Pseudocode:
# 1. Instantiate a class for the program.
# 2. Initialize an empty string in the init class.
# 3. Instantiate the method for raw input from the console.
# 4. Call the recursive function based on input.
# 5. Define the function for going through the string and building the list generated.
# 6. Use the recursive function to build the list sequence.


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
        elif current == 1:
            return 1
        else:
            return fibonacci(current - 1) + fibonacci(current - 2)
    else:
        return "Not a number!"


test = Prompt()
test.input()
solution = []
for i in range(int(test.entry) + 1):
    solution.append(str(fibonacci(i)))
print ", ".join(solution)
