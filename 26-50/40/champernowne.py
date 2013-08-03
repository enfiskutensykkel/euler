#!/usr/bin/env python

def digit(n):

	digits = ""
	current = 0
	while len(digits) < n:
		current += 1
		digits += str(current)

	return digits[n-1]

if __name__ == '__main__':
	product = 1
	for n in xrange(0, 7):
		product *= int(digit(10**n))
	print product
