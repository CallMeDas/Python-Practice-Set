'''Print a Cross Pattern of Stars with Diagonals
Difficulty: Hard
Topics: Pattern Printing
Hint: Print a cross pattern using stars with intersecting diagonals.

Example 1: Input: n = 5
Output:

* * * * *
 * * * *
  * * *
   * *
    *
   * *
  * * *
 * * * *
* * * * *
'''

def crossPattern(n):
    for i in range(n):
        print(" " * i + "* " * (n - i)) 

    for i in range(n - 2, -1, -1):
        print(" " * i + "* " * (n - i))  

crossPattern(5)
