'''Generating a Right-Angle Triangle Pattern of Numbers
Difficulty: Easy
Topics: Patterns
Description: Write a program to create a right-angle triangle pattern with numbers.
Example:
Input: height = 4
Output:

1  
12  
123  
1234  '''

def rightAngledTriangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end= '')
        print()


print(rightAngledTriangle(4))