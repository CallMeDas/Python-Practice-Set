'''Calculating the Sum of a Series (1 + 1/2 + 1/3 + ... + 1/n)
Difficulty: Medium
Topics: Mathematical Computations
Description: Write a program to calculate the sum of the series 1 + 1/2 + 1/3 + ... + 1/n up to the nth term.
Example:
Input: n = 4
Output: 2.083333
Explanation: Sum of the series is 1 + 1/2 + 1/3 + 1/4 ≈ 2.083333.'''

def sumOfSeries(n):
    s = 0
    for i in range(1, n + 1):
        s = s + (1/i)
    return s

print(sumOfSeries(4))

