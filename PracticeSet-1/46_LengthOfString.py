'''Determining the Length of a String Without Using Built-In Functions
Difficulty: Medium
Topics: String Manipulation
Description: Write a program to determine the length of a string without using built-in functions.
Example:
Input: string = "hello"
Output: 5
Explanation: The length of the string "hello" is determined without using built-in functions.'''

def lenthString(str1):
    c= 0
    for i in str1:
        c += 1
    return c

print(lenthString('hello'))
