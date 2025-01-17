'''Finding the Fibonacci Number at a Specific Position
Difficulty: Easy
Topics: Basic Programming, Sequences
Description: Write a program to find the Fibonacci number at a specific position.
Example:
Input: position = 5
Output: 5
Explanation: The Fibonacci number at position 5 is 5 (sequence: 0, 1, 1, 2, 3, 5).'''


def fibonacciAtPosition(n):
    a, b = 0, 1
    for i in range(0, n +1 ):
        if i == n:
            return a
        else:
            c = a + b
            a = b
            b = c

print(fibonacciAtPosition(5))

