'''Checking if a Number is a Narcissistic Number
Difficulty: Easy
Topics: Basic Programming, Number Theory
Description: Write a program to check if a number is a narcissistic number (where the sum of its digits raised to the power of the number of digits equals the number itself).
Example:
Input: number = 153
Output: Narcissistic Number
Explanation: 153 is a narcissistic number because 1^3 + 5^3 + 3^3 = 153.
'''

def narcissisticNo(n):

    t = n
    c = 0
    s = 0
    while t != 0:
        t = t // 10
        c += 1
    
    temp = n
    while temp != 0:
        r = temp % 10
        s = s + pow(r,c)
        temp = temp // 10
    if s == n:
        return 'Narcissistic Number '
    else:
        return 'Not Narcissistic Number'



print(narcissisticNo(153))
