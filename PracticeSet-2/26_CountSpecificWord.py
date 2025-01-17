'''Finding the Count of a Specific Word in a String
Difficulty: Easy
Topics: String Manipulation
Description: Write a program to count how many times a specific word appears in a given string.
Example:
Input: string = "hello world hello"
Output: 2
Explanation: The word "hello" appears 2 times in the string.
'''

def count_word_occurrences(string, word):
    words = string.split()
    return words.count(word)


string = "hello world hello"
word = "hello"
result = count_word_occurrences(string, word)
print(result)
