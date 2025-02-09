'''Print a Right-Angle Triangle of Numbers
Difficulty: Easy
Topics: Pattern Printing
Hint: Print a right-angle triangle pattern with increasing numbers. Each row should contain a continuous sequence of increasing numbers.

Example 1: Input: n = 4
Output:

1
23
456
78910
'''

def rightAngled(n):
    num = 1
    for i in range (1, n + 1):
        for j in range (i):
            print(num, end= '')
            num += 1
        print()


rightAngled(4)