"""
File: palindrome.py
Author: Wade Chao
----------------------------
This program prints the answers of whether
'madam', 'step on no pets', 'Q', 'pythonyp', and
'notion' are palindrome using a recursive function
called is_palindrome(s).
What is the self-similarity in this problem?
"""


def main():
	print(is_palindrome('madam'))             # True
	print(is_palindrome('step on no pets'))   # True
	print(is_palindrome('Q'))                 # True
	print(is_palindrome('pythonyp'))          # False
	print(is_palindrome('notion'))            # False


def is_palindrome(s):
	"""
	1. What's the base case
	2. Self Similarity
	"""
	if len(s) == 0 or len(s) == 1:
		return True
	else:
		if s[0] != s[-1]:
			return False
		else:
			return is_palindrome(s[1:-1])


if __name__ == '__main__':
	main()
