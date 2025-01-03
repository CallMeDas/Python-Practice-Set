'''Generating a Fibonacci Sequence Using Recursion
Difficulty: Medium
Topics: Recursion, Sequences
Description: Write a recursive program to generate the Fibonacci sequence up to a given number.
Example:
Input: number = 5
Output: 0, 1, 1, 2, 3
Explanation: The Fibonacci sequence up to 5 is generated.'''

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1)+ fibo(n - 2)
    
x = 5
for i in range(0 ,x +1 ):
    print(fibo(i))

    