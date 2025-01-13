'''Finding the GCD of Multiple Numbers
Difficulty: Medium
Topics: Mathematical Computations
Description: Write a program to find the GCD (Greatest Common Divisor) of an array of numbers.
Example:
Input: array = [12, 24, 36]
Output: 12
Explanation: The GCD of 12, 24, and 36 is 12.'''

from math import gcd
from functools import reduce

def findGCD(array):
    return reduce(gcd, array)

array = [12, 24, 36]
result = findGCD(array)
print(f"The GCD of {array} is {result}")
