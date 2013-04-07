#!/usr/bin/env python

# Bruteforce answer, because I'm lazy

def base10palindrome(n):
	return str(n)[::-1] == str(n)

def base2palindrome(n):
	s = bin(n)[2:]
	return s[::-1] == s

num = 0
for n in xrange(1, 10**6):
	if base10palindrome(n) and base2palindrome(n):
		num += n

print num
