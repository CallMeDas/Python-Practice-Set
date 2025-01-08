'''Finding the Longest Substring Without Repeating Characters
Difficulty: Medium
Topics: String Manipulation, Sliding Window
Description: Write a program to find the longest substring without repeating characters in a given string.
Example:
Input: string = "abcabcbb"
Output: "abc"
Explanation: The longest substring without repeating characters is "abc".'''

def longestUniqueSubstring(s):
    start = 0
    max_length = 0
    max_substring = ""
    seen = {}

    for end, char in enumerate(s):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1  
        seen[char] = end  
        current_length = end - start + 1

        if current_length > max_length:
            max_length = current_length
            max_substring = s[start:end + 1]

    return max_substring


print(longestUniqueSubstring("abcabcbb"))
