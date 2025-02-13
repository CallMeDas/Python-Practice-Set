'''Print a Matrix with Zigzag Pattern
Difficulty: Hard
Topics: Matrix Pattern
Hint: Print a matrix with a zigzag pattern of numbers. The numbers should alternate direction row-wise.

Example 1: Input: n = 3
Output:

1 2 3 4
8 7 6 5
9 10 11 12
'''

def zigZagPattern(n):
    num = 1
    for i in range(n):
        for j in range(n + 1):
            print(num, end=' ')
            num += 1
        print()


zigZagPattern(3)