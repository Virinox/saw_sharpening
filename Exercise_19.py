# Exercise 19
# Level 3
# written by: Vince Mao
# last modified: 2019.4.30
# Description:
# Write a program to sort the (name, age, score) tuples by ascending order where
# name is a string and age and score are numbers. The tuples are input by console. The sorting criteria are:
# 1: Sort by name
# 2: Then sort by age
# 3: Then sort by score
# The priority is name > age > score.
# Your program should accept a multiple line input of comma-separated tuples.
#
# Example:
# Given the following input:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# The output should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
#
# Hint:
# The data should be assumed to be a console input.
# Use the itemgetter() and attrgetter() methods from the operator package.
#
# Pseudocode:
# 1. Instantiate a class for the program.
# 2. Instantiate the method for multiple line input from the console.
# 3. Instantiate the method for parsing each tuple input.
# 4. Use a for loop to go through the entries and build the tuple lists.
# 5. Use the itemgetter method to sort by name, then by age, and finally by score.
# 6. Return the sorted list of tuples.

import sys
from operator import itemgetter


class ScoreSort:
    def __init__(self):
        self.entry = ""

    def input(self):
        print "Please input a sequence of tuples for the format of (name, age, score): "
        self.entry = sys.stdin.readlines()

    def process(self):
        solution = []
        tuple_list = []
        build = []
        if self.entry is not None:
            for line in self.entry:
                check = str(line).split(',')
                for i in range(3):
                    if i == 0:
                        build.append(str(check[i]))
                    else:
                        build.append(int(check[i]))
                tuple_list.append(tuple(build))
                build = []
            solution = sorted(tuple_list, key=itemgetter(0, 1, 2))

        return solution


test = ScoreSort()
test.input()
print test.process()
