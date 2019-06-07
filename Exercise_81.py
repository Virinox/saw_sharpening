# Exercise 81
# Level 1
# written by: Vince Mao
# last modified: 2019.6.6
# Description:
# Please write a program to print the runtime execution of  printing"1+1" 100 times.
#
# Hint:
# Use the timeit() module to measure the runtime.
# Use the Timer method to measure the runtime.
#
# Pseudocode:
# 1. Import time.
# 2. Use the timeit() module and the Timer function with proper syntax to print the runtime execution.


from timeit import Timer

test = Timer("for i in range(100): 1 + 1")
print test.timeit()
