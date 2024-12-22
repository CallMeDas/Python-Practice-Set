'''Generating the Fibonacci Series
Difficulty: Easy
Topics: Basic Programming, Sequences
Description: Write a program to generate the Fibonacci series up to a given number.
Example:
Input: limit = 10
Output: [0, 1, 1, 2, 3, 5, 8]
Explanation: The Fibonacci series up to 10 is generated as [0, 1, 1, 2, 3, 5, 8].'''

def fibo (n):
    a =0
    b =1
    for i in range (1, n+1):
        print(a)
        c= a + b
        a = b
        b = c

print(fibo(10))
