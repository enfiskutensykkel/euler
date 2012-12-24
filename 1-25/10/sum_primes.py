#!/usr/bin/env python

from math import sqrt

def sieve(n):
	numbers = range(0, n)
	primes = []

	m = sqrt(n)
	for i in xrange(2,n):
		if numbers[i]:
			primes.append(i)

			if i < m:
				for j in xrange(2 * i, n, i):
					numbers[j] = 0

	return primes



print sum(sieve(2*10**6))
