# Exercise 53
# Level 1
# written by: Vince Mao
# last modified: 2019.5.8
# Description:
# Define a class named Shape and its subclass Square. The Square class has an init function which takes a
# length as an argument. Both classes have an area function that prints the area of the shape.
# The class Shape's area is 0 by default.
#
# Hint:
# To override a method in the super class, define a method with the same name in the sub class.
#
# Pseudocode:
# 1. Instantiate a class called "Shape".
# 2. Instantiate the subclass "Square".
# 3. Define the init and area functions for both classes. Initialize the areas to 0.
# 4. The init function for Square has a length argument.
# 5. Return the area calculations.


class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        super(Square, self).__init__()
        self.length = length

    def area(self):
        return self.length * self.length


test = Square(6)
print test.area()
