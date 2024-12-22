'''Identifying Palindromes
Difficulty: Easy
Topics: Basic Programming, String Manipulation
Description: Write a program to check if a string or number is a palindrome.
Example:
Input: string = "radar"
Output: Palindrome
Explanation: "radar" reads the same backward as forward.'''

def palindrome(n):
    str = ''
    for i in n:
        str = i + str
    if str == n:
        return 'Palindrome'
    else:
        return 'NOt Palindrome'


print(palindrome('radar'))