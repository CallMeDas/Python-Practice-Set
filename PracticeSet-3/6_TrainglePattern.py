''' Print a Number Triangle
Difficulty: Easy
Topics: Pattern Printing
Hint: Print a right-angle triangle pattern with numbers. Each row should contain an increasing sequence of numbers starting from 1.

Example 1: Input: n = 4
Output:

1
12
123
1234
'''

def trainglePattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end= '')
        print()


trainglePattern(4)
