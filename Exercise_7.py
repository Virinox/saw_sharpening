# Exercise 7
# Level 2
# written by: Vince Mao
# last modified: 2019.4.22
# Description:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element in the ith row and jth column of the array should be i*j.
#
# Example:
# Given the following inputs:
# 3,5
# The output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
#
# Hint:
# The data should be assumed to be a console input.
#
# Pseudocode:
# 1. Instantiate a class for the program.
# 2. Initialize x and y dimensions to 0 in the init class.
# 3. Instantiate the method for raw input from the console for the array dimensions.
# 4. Instantiate the method for generating the array with the elements calculated.
# 5. Return the resulting array.


class Array:
    def __init__(self):
        self.row = 0
        self.col = 0
        self.entry = ""

    def input(self):
        self.entry = raw_input("Please input the x and y dimensions for array generation: ")

    def generate(self):
        if self.entry is not None:
            array = self.entry.split(',')
            if len(array) is not 2:
                return "Error in array dimensions!"
            for x in range(2):
                if not array[x].isdigit():
                    return "Error in list input!"

            self.row = int(array[0])
            self.col = int(array[1])
            row_solution = []
            col_solution = []

            for i in range(self.row):
                for j in range(self.col):
                    col_solution.append(i * j)
                row_solution.append(col_solution)
                col_solution = []

            return row_solution


test = Array()
test.input()
print test.generate()
