'''Checking for Anagram Pairs in a List of Strings
Difficulty: Medium
Topics: String Manipulation
Description: Write a program to find pairs of strings in a list that are anagrams of each other.
Example:
Input: strings = ["listen", "silent", "hello", "world"]
Output: [("listen", "silent")]
Explanation: "listen" and "silent" are anagrams.'''

def find_anagram_pairs(strings):
    anagram_pairs = []
    n = len(strings)
    
    for i in range(n):
        for j in range(i + 1, n):
            if sorted(strings[i]) == sorted(strings[j]):
                anagram_pairs.append((strings[i], strings[j]))
    return anagram_pairs

strings = ["listen", "silent", "hello", "world"]
result = find_anagram_pairs(strings)
print(result) 
