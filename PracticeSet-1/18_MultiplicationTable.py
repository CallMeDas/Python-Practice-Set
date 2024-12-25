'''Generating Multiplication Tables
Difficulty: Easy
Topics: Basic Programming, Mathematical Computations
Description: Write a program to generate multiplication tables for a given number.
Example:
Input: number = 4
Output:

4 x 1 = 4  
4 x 2 = 8  
4 x 3 = 12  
4 x 4 = 16  
4 x 5 = 20  
Explanation: The multiplication table for 4 up to 5 is generated.
'''

def multiTable(n):
    for i in range(1, 6):
        print( f'{n} x {i} = {n*i}')
    
multiTable(4)