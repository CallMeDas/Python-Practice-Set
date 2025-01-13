'''Counting the Number of Palindromic Substrings in a String
Difficulty: Medium
Topics: String Manipulation
Description: Write a program to count how many palindromic substrings exist in a given string.
Example:
Input: string = "aaa"
Output: 6
Explanation: Palindromic substrings are "a", "a", "a", "aa", "aa", "aaa".'''

def countPalindromicSubstrings(s):
    n = len(s)
    count = 0
    def countPalindromesAroundCenter(left, right):
        nonlocal count
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

    for i in range(n):
        countPalindromesAroundCenter(i, i)
        countPalindromesAroundCenter(i, i + 1)

    return count


string = "aaa"
print(countPalindromicSubstrings(string))
