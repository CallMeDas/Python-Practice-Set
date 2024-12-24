'''Finding the Least Common Multiple (LCM)
Difficulty: Easy
Topics: Basic Programming, Number Theory
Description: Write a program to find the LCM of two numbers.
Example:
Input: a = 12, b = 15
Output: 60
Explanation: The LCM of 12 and 15 is 60.'''


def lcm(a,b):
    min = a if a > b else b
    for i in range(1, min + 1):
        if  a % i == 0 and b % i == 0:
            hcf = i
    lcm = int ((a * b)/ hcf)
    return lcm

print(lcm(12, 15))