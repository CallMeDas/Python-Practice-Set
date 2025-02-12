'''Print a Cross Pattern with Stars
Difficulty: Medium
Topics: Pattern Printing
Hint: Print a cross pattern using stars. The cross should be centered within a matrix.

Example 1: Input: n = 5
Output:

***
  *
  *
  *
***
'''

def crossPattern(n):
    for i in range(n):
        for j in range(3):
            if i == 0 or i == n - 1 or j == n // 2:
                print("*", end="")
            else:
                print(" ", end="")
        print()  

crossPattern(5)