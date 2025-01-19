'''Finding the Count of Digits Greater Than a Specific Value
Difficulty: Easy
Topics: Mathematical Computations
Description: Write a program to count how many digits in a number are greater than a specific value.
Example:
Input: number = 54321, value = 3
Output: 2
Explanation: The digits
greater than 3 in 54321 are 5, 4, and 4, so the count is 2.'''

def count_digits_greater_than(number, value):
    count = 0
    for digit in str(number):
        if int(digit) > value:
            count += 1
    return count

number = 54321
value = 3
result = count_digits_greater_than(number, value)
print(f"The count of digits greater than {value} in {number} is: {result}")
