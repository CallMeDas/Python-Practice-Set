'''Finding the Largest Palindrome in a String
Difficulty: Easy
Topics: Basic Programming, String Manipulation
Description: Write a program to find the largest palindrome in a given string.
Example:
Input: string = "babad"
Output: "bab" or "aba"
Explanation: Both "bab" and "aba" are valid palindromes in the string.
'''

def largestPalindrome(string):
    def isPalindrome(s):
        return s == s[::-1]

    n = len(string)
    max_palindrome = ""
    
    for i in range(n):
        for j in range(i, n):
            substring = string[i:j + 1]
            if isPalindrome(substring) and len(substring) > len(max_palindrome):
                max_palindrome = substring

    return max_palindrome

print(largestPalindrome("babad"))
