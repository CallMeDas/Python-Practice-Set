'''Finding the Frequency of Each Character in a String
Difficulty: Easy
Topics: String Manipulation
Description: Write a program to count the frequency of each character in a given string.
Example:
Input: string = "hello"
Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
Explanation: The frequency of each character in the string "hello" is shown.'''

def character_frequency(string):
    frequency = {}
    for char in string:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency


string = "hello"
result = character_frequency(string)
print(result)
