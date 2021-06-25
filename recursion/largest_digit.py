"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""
import math


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	Find the largest digit from the given number
	:param n: int, A number that could be positive or negative
	:return: int or str, Return
	"""
	return find_largest_digit_helper(abs(n), -math.inf)


def find_largest_digit_helper(n, max_num):
	"""
	Using recursion to divide the number and get the max digit form it
	:param n: int, the number that should be divided and looked into the digit
	:param max_num: the maximum digit to compare with
	:return: the maximum digit in the number
	"""
	if n <= 0 or max_num == 9:
		return max_num
	else:
		new_max = n % 10 if n % 10 > max_num else max_num
		return find_largest_digit_helper(n//10, new_max)


if __name__ == '__main__':
	main()
