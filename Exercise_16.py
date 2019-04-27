# Exercise 16
# Level 2
# written by: Vince Mao
# last modified: 2019.4.27
# Description:
# Use list comprehension to square each odd number in a list and return the resulting list.
# The list is input by a sequence of comma-separated numbers.
#
# Example:
# Given the following input:
# 1,2,3,4,5,6,7,8,9
# The output should be:
# 1,9,25,49,81
#
# Hint:
# The data should be assumed to be a console input.
#
# Pseudocode:
# 1. Instantiate a class for the program.
# 2. Instantiate the method for raw input from the console.
# 3. Instantiate the method for checking if each element in the list is odd. If so, append the square to the solution.
# 4. Return the solution


class OddProduct:
    def __init__(self):
        self.entry = ""

    def input(self):
        self.entry = raw_input("Please input a comma-separated list of numbers: ")

    def process(self):
        result = []
        check = self.entry.split(",")
        for i in range(len(check)):
            if check[i].isdigit():
                continue
            else:
                return "Input has elements that are not integer numbers!"

        for j in range(len(check)):
            if int(check[j]) % 2 != 0:
                result.append(str(int(check[j]) * int(check[j])))
        return ",".join(result)


test = OddProduct()
test.input()
print test.process()
