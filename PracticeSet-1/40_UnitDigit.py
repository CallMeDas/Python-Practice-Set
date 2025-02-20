'''Calculating the Sum of Digits of a Number Until Single Digit
Difficulty: Medium
Topics: Mathematical Computations
Description: Write a program to keep summing the digits of a number until a single digit is obtained.
Example:
Input: number = 9875
Output: 2
Explanation: The sum of digits is 9 + 8 + 7 + 5 = 29, and then 2 + 9 = 11, and finally 1 + 1 = 2.'''

def singleDigit(n):
    while n > 9:
        s = 0
        while n != 0:
            s += n % 10
            n //= 10
        n = s  
    return n

print(singleDigit(9875))


