'''Finding the Difference Between the Sum of Even and Odd Numbers in an Array
Difficulty: Easy
Topics: Arrays, Mathematical Computations
Description: Write a program to calculate the difference between the sum of even and odd numbers in an array.
Example:
Input: array = [1, 2, 3, 4, 5, 6]
Output: 3
Explanation: The sum of even numbers is 12, and the sum of odd numbers is 9. The difference is 3.'''


def difference_even_odd(array):
    even_sum = sum(num for num in array if num % 2 == 0)
    odd_sum = sum(num for num in array if num % 2 != 0)
    return even_sum - odd_sum

array = [1, 2, 3, 4, 5, 6]
result = difference_even_odd(array)
print("Difference:", result)
