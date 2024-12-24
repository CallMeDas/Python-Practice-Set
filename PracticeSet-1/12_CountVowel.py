'''Counting Vowels and Consonants in a String
Difficulty: Easy
Topics: Basic Programming, String Manipulation
Description: Write a program to count vowels and consonants in a given string.
Example:
Input: string = "hello world"
Output: Vowels: 3, Consonants: 7
Explanation: "hello world" contains 3 vowels (e, o, o) and 7 consonants (h, l, l, w, r, l, d).'''

def countVowel(str):
    vowel = 'aeiou'
    vol = 0
    cons = 0
    str = str.lower().replace(' ', '')
    for i in str:
        if i.isalpha():
            if i in vowel:
                vol += 1
            else:
                cons += 1
    return f'Vowel : {vol} \nconsonant : {cons}'




print(countVowel('hello world'))