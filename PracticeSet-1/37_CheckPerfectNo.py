'''Checking for Perfect Squares
Difficulty: Easy
Topics: Mathematical Computations
Description: Write a program to determine if a number is a perfect square.
Example:
Input: number = 16
Output: True
Explanation: 16 is a perfect square (4^2 = 16).'''

import math
def checkPerfectNo(n):
    num = math.isqrt(n)

    return num * num == n
    
print(checkPerfectNo(4))