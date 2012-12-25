#!/usr/bin/env python
#coding=utf8

# this takes some time to run
# it's not very efficient and quite naive, but it works

from math import sqrt

def sieve(N):
	numbers = range(0, N)
	primes = []

	for i in xrange(2, int(sqrt(N))):
		if numbers[i] != 0:
			for j in xrange(i + i, N, i):
				numbers[j] = 0

	for i in xrange(2, N):
		if numbers[i] != 0:
			primes.append(i)

	return primes

def test(primes, a, b):
	n = 0
	while True:
		t = (n**2 + a*n + b)
		if t > primes[-1]:
			primes = sieve(t*2)

		if not t in primes:
			break

		n += 1

	return n-1


if __name__ == '__main__':
	primes = [1] + sieve(1000)

	a_mark = 1
	b_mark = 1
	n = 0

	for p in primes:
		for q in primes:

			for a in (-p, p):
				for b in (-q, q):
					m = test(primes, a, b)
					if m > n:
						n = m
						a_mark = a
						b_mark = b

	print a_mark, b_mark, n
	print a_mark * b_mark
