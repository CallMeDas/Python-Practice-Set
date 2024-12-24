'''Reversing a String
Difficulty: Easy
Topics: Basic Programming, String Manipulation
Description: Write a program to reverse a given string.
Example:
Input: string = "programming"
Output: "gnimmargorp"
Explanation: The reversed string of "programming" is "gnimmargorp".'''

def reverseString(str):
    str1 = ''
    for i in str:
        str1 = i + str1
    
    return str1


print(reverseString('programming'))