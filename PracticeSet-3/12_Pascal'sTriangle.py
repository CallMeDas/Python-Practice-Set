'''Print a Pascal’s Triangle
Difficulty: Medium
Topics: Matrix Pattern
Hint: Print Pascal’s Triangle up to N rows. Each row should be constructed based on the sum of the elements directly above it in the previous row.

Example 1: Input: n = 4
Output:

   1
  1 1
 1 2 1
1 3 3 1
'''

def pascalsTriangle(n):
    triangle = [[1] * (i + 1) for i in range(n)]
    
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    
    for i in range(n):
        print(" " * (n - i), end="")
        print(" ".join(map(str, triangle[i])))

pascalsTriangle(4)
