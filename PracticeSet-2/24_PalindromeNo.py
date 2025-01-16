'''Checking for Palindromic Numbers in a Range
Difficulty: Medium
Topics: Mathematical Computations
Description: Write a program to check for palindromic numbers within a given range.
Example:
Input: start = 1, end = 100
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99]
Explanation: Palindromic numbers between 1 and 100 are the numbers listed.'''

def find_palindromic_numbers(start, end):
    palindromic_numbers = []
    for number in range(start, end + 1):
        if str(number) == str(number)[::-1]: 
            palindromic_numbers.append(number)
    return palindromic_numbers

start = 1
end = 100
result = find_palindromic_numbers(start, end)
print("Palindromic numbers in the range:", result)

