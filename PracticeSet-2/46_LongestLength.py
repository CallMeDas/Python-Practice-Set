'''Finding the Length of the Longest Word in a String
Difficulty: Easy
Topics: String Manipulation
Description: Write a program to find the length of the longest word in a given string.
Example:
Input: string = "Find the longest word"
Output: 7
Explanation: The longest word is "longest" with length 7.
'''
def longestLength(string):
    words = string.split()
    max_length = max(len(word) for word in words)
    return max_length


string = "Find the longest word"
result = longestLength(string)
print(result)
