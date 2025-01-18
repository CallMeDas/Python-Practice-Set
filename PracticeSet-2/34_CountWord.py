'''Finding the Number of Words in a String
Difficulty: Easy
Topics: String Manipulation
Description: Write a program to count the number of words in a given string.
Example:
Input: string = "Hello world"
Output: 2
Explanation: There are 2 words in the string.'''

def count_words(string):
    words = string.split()
    return len(words)


string = "Hello world"
result = count_words(string)
print(result)
