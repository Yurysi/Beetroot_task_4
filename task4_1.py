"""
Task 1

Write a Python program to get a string made of the first 2 and the
last 2 chars from a given string. If the string length is less than
2, return instead of the empty string.
"""

strings_task = ['helloworld', 'my', 'x']

for string_task in strings_task:
    long_string = string_task[:2] + string_task[-2:]

    if 2 <= len(string_task):
        print(long_string)

    else:
        print("Empty String")
