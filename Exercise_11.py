# Exercise 11
# Level 2
# written by: Vince Mao
# last modified: 2019.4.24
# Description:
# Write a program which accepts a sequence of comma-separated 4-digit binary numbers
# as its input and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma-separated sequence.
#
# Example:
# Given the following input:
# 0100,0011,1010,1001
# The output should be:
# 1010
#
# Hint:
# The data should be assumed to be a console input.
#
# Pseudocode:
# 1. Instantiate a class for the program.
# 2. Initialize an empty string in the init class.
# 3. Instantiate the method for raw input from the console for the 4-digit binary number list.
# 4. Instantiate the method for generating the list that parses all numbers using the comma as a separator.
# 5. Check to see if the number is binary and a multiple of 5 and add to the solution list if so.
# 6. Return the solution list.


class BinaryCheck:
    def __init__(self):
        self.entry = ""

    def input(self):
        self.entry = raw_input("Please input a string of 4-digit binary numbers: ")

    def process(self):
        solution = []
        if self.entry is not None:
            check = self.entry.split(",")
            for nums in check:
                if len(nums) != 4 or not bin(int(nums)):
                    return None
                else:
                    if int(nums, 2) % 5 == 0:
                        solution.append(nums)
        return ' '.join(solution)


test = BinaryCheck()
test.input()
print test.process()
