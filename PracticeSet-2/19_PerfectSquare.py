'''Checking for Perfect Squares in a Range
Difficulty: Easy
Topics: Mathematical Comput

ations
Description: Write a program to check which numbers in a given range are perfect squares.
Example:
Input: start = 1, end = 10
Output: [1, 4, 9]
Explanation: Perfect squares between 1 and 10 are 1, 4, and 9.'''

def find_perfect_squares(start, end):
    perfect_squares = []


    current = int(start**0.5)

    while current**2 <= end:
        if current**2 >= start:
            perfect_squares.append(current**2)
        current += 1

    return perfect_squares

start = 1
end = 10
output = find_perfect_squares(start, end)
print(output)
