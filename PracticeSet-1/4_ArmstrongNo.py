'''Calculating Armstrong Numbers
Difficulty: Easy
Topics: Basic Programming, Number Theory
Description: Write a program to check if a number is an Armstrong number.
Example:
Input: number = 153
Output: Armstrong Number
Explanation: 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.'''

def armstrongNo(n):

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
        return 'Armstong '
    else:
        return 'Not Armstrong'



print(armstrongNo(370))

    
