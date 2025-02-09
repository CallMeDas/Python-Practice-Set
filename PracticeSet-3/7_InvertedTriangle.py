'''Print an Inverted Triangle Pattern
Difficulty: Easy
Topics: Pattern Printing
Hint: Print an inverted triangle pattern with stars (*). Each row should contain decreasing numbers of stars from the top row.

Example 1: Input: n = 5
Output:

*****
 ****
  ***
   **
    *
    '''

def invertedTriangle(n):
    for i in range(n):
        print(" " * i + "*" * (n - i))


invertedTriangle(5)
