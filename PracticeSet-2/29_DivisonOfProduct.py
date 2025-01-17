'''Finding All Divisors of the Product of Two Numbers
Difficulty: Medium
Topics: Number Theory
Description: Write a program to find all divisors of the product of two given numbers.
Example:
Input: number1 = 6, number2 = 10
Output: [1, 2, 3, 5, 6, 10, 12, 15, 20, 30, 60]
Explanation: The product of 6 and 10 is 60, and its divisors are listed.'''

def divisionProduct(a , b):
    divisor = []
    p = a * b
    for i in range(1, p + 1):
        if p % i == 0:
            divisor.append(i)
    return divisor


print(divisionProduct(6, 10))
