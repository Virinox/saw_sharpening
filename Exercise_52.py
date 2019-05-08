# Exercise 52
# Level 1
# written by: Vince Mao
# last modified: 2019.5.8
# Description:
# Define a class named Rectangle which can be constructed by a length and width.
# The Rectangle class has a method which can compute the area.
#
# Hint:
# Use def methodName(self) to define a method.
#
# Pseudocode:
# 1. Instantiate a class called "Rectangle".
# 2. Instantiate the method to compute the area of the rectangle using the length and width.


class Rectangle(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


test = Rectangle(6, 4)
print test.area()
