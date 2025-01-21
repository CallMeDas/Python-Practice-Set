'''Generating a Pattern of Increasing Numbers
Difficulty: Easy
Topics: Patterns
Description: Write a program to create a pattern where numbers increase with each row.
Example:
Input: rows = 3
Output:

1  
12  
123  '''

def pattern(n):
    for i in range (1, n + 1):
        for j in range(1, i + 1):
            print(j, end='')
        print()



print(pattern(3))