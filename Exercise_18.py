# Exercise 18
# Level 3
# written by: Vince Mao
# last modified: 2019.4.28
# Description:
# A website requires the users to input a username and password to register.
# Write a program to check the validity of the password input by users.
# The password must meet the following criteria:
# 1. Contain at least 1 lower case letter
# 2. Contain at least 1 integer number
# 3. Contain at least 1 upper case letter
# 4. Contain at least 1 special character from [$#@]
# 5. Contain 6 - 12 characters
# Your program should accept a sequence of comma-separated passwords and will check them based on the criteria.
# Passwords that match the criteria are to be printed in a comma-separated format
#
# Example:
# Given the following input:
# ABd1234@1,a F1#,2w3E*,2We3345
# The output should be:
# ABd1234@1
#
# Hint:
# The data should be assumed to be a console input.
# Use the regular expression package.
#
# Pseudocode:
# 1. Instantiate a class for the program.
# 2. Instantiate the method for parsing the comma-separated list of passwords.
# 3. Instantiate the method for looping through the items in the list.
# 4. Use if statements to see if the element meets the password criteria. If so, add it to the solution list.
# 5. Return the list as a comma-separated list of passwords that fulfill the criteria.

import re


class PasswordCheck:
    def __init__(self):
        self.entry = ""

    def input(self):
        self.entry = raw_input("Please input a comma-separated list of candidate passwords: ")

    def process(self):
        solution = []
        check = self.entry.split(",")
        for i in range(len(check)):
            if re.search('\s', check[i]) or len(check[i]) < 6 or len(check[i]) > 12:
                break
            if re.search("[a-nA-N]", check[i]):
                if re.search("[0-9]", check[i]):
                    if re.search("[$#@]", check[i]):
                        solution.append(check[i])

        return ','.join(solution)


test = PasswordCheck()
test.input()
print test.process()
