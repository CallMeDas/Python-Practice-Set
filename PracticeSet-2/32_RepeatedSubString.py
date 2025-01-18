'''Checking for a Repeated Substring in a String
Difficulty: Medium
Topics: String Manipulation
Description: Write a program to check if a substring is repeated within a given string.
Example:
Input: string = "abab"
Output: True
Explanation: The substring "ab" is repeated.'''

def has_repeated_substring(s):
    n = len(s)
    for i in range(1, n // 2 + 1): 
        if n % i == 0:
            substring = s[:i]
            if substring * (n // i) == s:
                return True
    return False


string = "abab"
result = has_repeated_substring(string)
print(result) 