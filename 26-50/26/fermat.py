#!/usr/bin/env python

from math import sqrt

# use sieve of Eratosthenes to find primes
def eratosthenes(n):
	numbers = range(0, n)
	primes = set()

	for i in xrange(2, int(sqrt(n))):
		if numbers[i]:
			for j in xrange(2*i, n, i):
				numbers[j] = 0

	for i in xrange(2, n):
		if numbers[i]:
			primes.add(i)

	return primes

# Fermat's little theorem to determine length of cycle
def fermat(p):
	for n in xrange(1, p):
		if 10**n % p == 1:
			return n

	return 0


if __name__ == '__main__':
	print reduce(lambda x, y: x if x[1] > y[1] else y, [(d, fermat(d)) for d in eratosthenes(1000)])
