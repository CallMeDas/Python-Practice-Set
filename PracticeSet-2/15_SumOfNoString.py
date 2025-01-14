'''Finding the Sum of Numbers in a String
Difficulty: Easy
Topics: String Manipulation
Description: Write a program to extract and sum all numbers present in a given string.
Example:
Input: string = "The numbers are 12 and 34"
Output: 46
Explanation: The sum of numbers 12 and 34 is 46.'''

import re

def sum_of_numbers_in_string(string):
    numbers = re.findall(r'\d+', string)

    return sum(map(int, numbers))

input_string = "The numbers are 12 and 34"
result = sum_of_numbers_in_string(input_string)
print(f"The sum of numbers in the string is: {result}")
