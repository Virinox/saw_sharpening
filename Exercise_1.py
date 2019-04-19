# Exercise 1
# Level 1
# written by: Vince Mao
# last modified: 2019.4.18
# Description:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
#
# Hint:
# Consider using the range(#begin, #end) method.

# Pseudocode:
# 1. Initialize an empty list
# 2. Loop from 2000 to 3201
# 3. Check if the number is divisible by 7 but not 5
# 4. If true, append to the list
# 5. Else, ignore
# 6. Return the list

result = []

for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        result.append(i)

print result
