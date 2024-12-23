'''Finding the Greatest Common Divisor (GCD)
Difficulty: Easy
Topics: Basic Programming, Number Theory
Description: Write a program to find the GCD of two numbers.
Example:
Input: a = 48, b = 18
Output: 6
Explanation: The GCD of 48 and 18 is 6.'''

def GDC (a, b):
    min = a if a < b else b
    for i in range (1, min + 1):
        if a % i == 0 and b % i == 0:
            hcf = i
    return hcf

print(GDC(48, 18))