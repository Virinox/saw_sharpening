# Exercise 51
# Level 1
# written by: Vince Mao
# last modified: 2019.5.8
# Description:
# Define a class named Circle which can be constructed by a radius.
# The Circle class has a method which can compute the area.
#
# Hint:
# Use def methodName(self) to define a method.
#
# Pseudocode:
# 1. Instantiate a class called "Circle".
# 2. Instantiate the method to compute the area of the circle using the radius.

import math


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


test = Circle(6)
print test.area()
