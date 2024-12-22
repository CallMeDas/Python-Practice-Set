'''Validating Leap Years
Difficulty: Easy
Topics: Basic Programming, Date Handling
Description: Write a program to check if a given year is a leap year.
Example:
Input: year = 2020
Output: Leap Year
Explanation: 2020 is divisible by 4 but not by 100, or it is divisible by 400, so it is a leap year.'''


def leapYear(n):
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        return 'Leap Year'
    else :
        return 'Not Leap Year'
    

print(leapYear(2000))