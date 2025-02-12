'''Print a Border Pattern with Numbers
Difficulty: Medium
Topics: Matrix Pattern
Hint: Print a border pattern using numbers. The border should be filled with numbers, and the inner part should be empty.

Example 1: Input: n = 4
Output:

1234
1  1
1  1
1234
'''

def borderPattern(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print(j + 1, end="")
            else:
                print(" ", end="")
        print()

borderPattern(4)
