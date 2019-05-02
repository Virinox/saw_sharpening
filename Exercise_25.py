# Exercise 25
# Level 1
# written by: Vince Mao
# last modified: 2019.5.2
# Description:
# Instantiate a class that has a class parameter and the same instance parameter.
#
# Hint:
# Define an instance parameter by adding it in the __init__ method.
# You can initiate an object with a constructor or set the value later.
#
# Pseudocode:
# 1. Instantiate a class.
# 2. Instantiate the __init__ method.
# 3. Assign a parameter in the method.


class Test:
    test = "Nothing"

    def __init__(self, entry=None):
        self.value = entry

    def generate(self):
        return self.value


test = Test()
print test.generate()
