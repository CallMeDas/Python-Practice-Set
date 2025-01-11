'''Finding the Sum of Digits of a Number Until Zero
Difficulty: Easy
Topics: Basic Programming, Mathematical Computations
Description: Write a program to repeatedly sum the digits of a number until the result is zero.
Example:
Input: number = 123
Output: 6
Explanation: Sum of digits is 1 + 2 + 3 = 6; sum of digits of 6 is 6 (which is a single digit).'''

def sumOfDigit(n):
    s = 0
    while n != 0:
        r = n % 10
        s = r + s
        n = n // 10
    return s


print(sumOfDigit(1234))