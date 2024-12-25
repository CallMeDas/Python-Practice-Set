'''Checking for Armstrong Numbers in a Range
Difficulty: Easy
Topics: Basic Programming, Number Theory
Description: Write a program to find all Armstrong numbers within a given range.
Example:
Input: range = [1, 500]
Output: [1, 153, 370, 371, 407]
Explanation: Armstrong numbers between 1 and 500 are 1, 153, 370, 371, and 407.'''

def armstrongRange(start, end):
    arm = []
    for i in range (start, end):
        t = i
        c = 0
        s = 0
        while t != 0:
            t = t // 10
            c += 1
    
        temp = i
        while temp != 0:
            r = temp % 10
            s = s + pow(r,c)
            temp = temp // 10
        if i == s:
            arm.append(i)
    return arm
           
        

print(armstrongRange(1, 500))