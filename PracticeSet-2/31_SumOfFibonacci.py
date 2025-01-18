'''Calculating the Sum of the First N Fibonacci Numbers
Difficulty: Medium
Topics: Fibonacci Sequence, Mathematical Computations
Description: Write a program to calculate the sum of the first N Fibonacci numbers.
Example:
Input: N = 5
Output: 12
Explanation: The first 5 Fibonacci numbers are 1, 1, 2, 3, 5, and their sum is 12.'''


def fiboSum (n):
    a =0
    b =1
    s = 0
    for i in range (1, n+1):
        c= a + b
        a = b
        b = c
        s = s + a
    return s


print(fiboSum(5))