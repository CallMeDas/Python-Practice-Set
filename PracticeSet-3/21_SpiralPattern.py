'''Print a Spiral Matrix
Difficulty: Hard
Topics: Matrix Pattern
Hint: Print a matrix filled with numbers in a spiral pattern. The numbers should start from 1 and increment as you move around the spiral.

Example 1: Input: n = 3
Output:

1 2 3
8 9 4
7 6 5
'''

def spiralPattern(n):
    num =  1
    for i in range (n):
        for j in range (n):
            print(num, end=' ')
            num += 1
        print()


spiralPattern(3)