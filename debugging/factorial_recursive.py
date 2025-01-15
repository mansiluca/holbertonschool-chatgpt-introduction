#!/usr/bin/python3
import sys

def factorial(n):
	"""
	Calculate the factorial of a given number using recursion.

	Parameters:
	n (int): The number for which the factorial is to be calculated. Must be a non-negative integer.

	Returns:
	int: The factorial of the given number. Returns 1 if the number is 0.
	"""
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)