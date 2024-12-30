'''Calculating the Power of a Number
Difficulty: Easy
Topics: Basic Programming, Mathematical Computations
Description: Write a program to calculate the power of a number.
Example:
Input: base = 2, exponent = 3
Output: 8
Explanation: 2 raised to the power of 3 is 8.'''

def powerOfNo(b, p):
    res = 1

    for i in  range (1, p + 1):
        res *= b
    return res


print(powerOfNo(2,3))
    