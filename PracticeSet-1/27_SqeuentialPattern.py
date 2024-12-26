'''Generating a Pattern of Numbers
Difficulty: Easy
Topics: Basic Programming, Patterns
Description: Write a program to generate number patterns (e.g., sequential numbers in a matrix).
Example:
Input: rows = 3
Output:

1  
2 3  
4 5 6 '''


def sequentialPattern(n):
     num = 1
     for i in range (1, n + 1):
            for j in range (i):
               print(num , end= ' ')
               num +=1
            print()
    
sequentialPattern(3)