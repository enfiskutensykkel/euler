#!/usr/bin/env python

def gcd(a, b):
	while a:
		a, b = b % a, a

	return b

n = 1
for i in xrange(1, 21):
	n = n * i / gcd(i, n)

print n
