# Exercise 80
# Level 1
# written by: Vince Mao
# last modified: 2019.6.3
# Description:
# Please write a program to compress and decompress the following string:
# "hello world!hello world!hello world!hello world!".
#
# Hint:
# Use the zlib.compress() and zlib.decompress() methods respectively to compress and decompress a string.
#
# Pseudocode:
# 1. Initialize the string.
# 2. Compress the string using the zlib.compress() method.
# 3. Print the compressed string to verify its compression.
#  4. Decompress and print the string using the zlib.decompress() method.


import zlib

test_String = "hello world!hello world!hello world!hello world!"
check = zlib.compress(test_String)
print check
print zlib.decompress(check)
