'''Generating a Number Pyramid
Difficulty: Medium
Topics: Patterns, Basic Programming
Description: Write a program to generate a pyramid of numbers (e.g., 1, 12, 123, etc.).
Example:
Input: rows = 4
Output:

1  
12  
123  
1234  
Explanation: A number pyramid with 4 rows is generated.'''

def pyramid(n):
    for i in range(1, n + 1):
        for j in range (1, i+1):
            print(j, end= '')
        print()


print(pyramid(4))