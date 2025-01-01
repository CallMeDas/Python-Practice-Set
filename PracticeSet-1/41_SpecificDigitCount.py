'''Finding the Count of Specific Digits in a Number
Difficulty: Easy
Topics: Basic Programming, String Manipulation
Description: Write a program to count the occurrences of a specific digit in a number.
Example:
Input: number = 122333, digit = 3
Output: 3
Explanation: The digit 3 occurs 3 times in the number 122333.'''

def specificDigitCount(n , d):
    n = str(n)
    d = str(d)

    return n.count(d)

print(specificDigitCount(122333, 3))