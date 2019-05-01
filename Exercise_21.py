# Exercise 21
# Level 3
# written by: Vince Mao
# last modified: 2019.4.30
# Description:
# A robot moves in a plane starting from the original point (0,0).
# The robot can move toward UP, DOWN, LEFT and RIGHT followed by defined distance value in steps.
# Write a program to calculate the distance from original position after a sequence of movements is given.
# If the distance is a float, round to the nearest integer.
# Example:
# Given the following input:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The output should be:
# 2
#
# Hint:
# The data should be assumed to be a console input.
# Use sqrt in the math package to calculate distance.
#
# Pseudocode:
# 1. Instantiate a class for the robot.
# 2. Instantiate the method that requests the sequence of movement in a multiple line input.
# 3. Instantiate the method for parsing the input and calculating the final distance.
# 4. Return the final distance value as an integer.

import sys
from math import sqrt


class RobotSequence:
    def __init__(self):
        self.entry = ""
        self.x = 0
        self.y = 0

    def input(self):
        print "Please input a movement sequence for the robot using the following format: "
        print "UP, DOWN, LEFT, RIGHT and the distance (if not an integer, it will be rounded)"
        self.entry = sys.stdin.readlines()

    def generate(self):
        if self.entry is not None:
            for line in self.entry:
                check = str(line).split()
                if check[0] not in ["UP", "DOWN", "LEFT", "RIGHT"]:
                    return "Direction input error!"
                if not check[1].isdigit():
                    return "Distance value error!"
                if check[0] == "UP":
                    self.y += int(check[1])
                if check[0] == "DOWN":
                    self.y -= int(check[1])
                if check[0] == "LEFT":
                    self.x -= int(check[1])
                if check[0] == "RIGHT":
                    self.x += int(check[1])
        distance = sqrt(self.x ** 2 + self.y ** 2)
        return int(round(distance))


test = RobotSequence()
test.input()
print test.generate()
