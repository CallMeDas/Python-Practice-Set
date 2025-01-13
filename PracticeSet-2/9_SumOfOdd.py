'''Finding the Sum of the First N Odd Numbers
Difficulty: Easy
Topics: Mathematical Computations
Description: Write a program to calculate the sum of the first N odd numbers.
Example:
Input: N = 5
Output: 25
Explanation: Sum of the first 5 odd numbers (1 + 3 + 5 + 7 + 9) is 25.'''

def oddSum(n):
    s = 0
    count = 0
    num = 1   

    while count < n: 
        s += num
        count += 1
        num += 2 

    return s

print(oddSum(5))  
