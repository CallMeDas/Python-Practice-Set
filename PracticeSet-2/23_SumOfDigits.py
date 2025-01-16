'''Finding the Sum of Digits of the Product of Two Numbers
Difficulty: Easy
Topics: Mathematical Computations
Description: Write a program to find the sum of the digits of the product of two given numbers.
Example:
Input: number1 = 12, number2 = 34
Output: 9
Explanation: The product of 12 and 34 is 408, and the sum of its digits is 4 + 0 + 8 = 12.
'''

def sum_of_digits_of_product(number1, number2):
    product = number1 * number2
    digit_sum = sum(int(digit) for digit in str(product))
    return digit_sum

number1 = 12
number2 = 34
result = sum_of_digits_of_product(number1, number2)
print("The sum of the digits of the product is:", result)

