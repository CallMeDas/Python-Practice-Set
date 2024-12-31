'''Finding the N-th Triangular Number
Difficulty: Easy
Topics: Basic Programming, Mathematical Computations
Description: Write a program to find the N-th triangular number.
Example:
Input: N = 4
Output: 10
Explanation: The 4th triangular number is 10 (sum of the first 4 natural numbers).
'''

def NthTrangularNo(n):
    return  n * (n+1) // 2


print(NthTrangularNo(4))