#!/usr/bin/env python
#coding=utf8

from math import sqrt

# naive bruteforcing of truncatability
def truncatable(p, primes):
	ltrunc = True
	rtrunc = True

	pstr = "%d" % p
	while len(pstr) > 0:
		if primes[int(pstr)] == 0:
			ltrunc = False
			break
		pstr = pstr[1:]

	pstr = "%d" % p
	while ltrunc and len(pstr) > 0:
		if primes[int(pstr)] == 0:
			rtrunc = False
			break
		pstr = pstr[:-1]

	return ltrunc and rtrunc


# sieve of eratosthenes
numbers = range(0,1000000)
numbers[1] = 0
for i in xrange(2, int(sqrt(len(numbers)))):
	if numbers[i]:
		for j in xrange(2*i, len(numbers), i):
			numbers[j] = 0


truncs = []
for i in xrange(2, len(numbers)):
	if numbers[i]:
		if truncatable(i, numbers):
			truncs.append(i)


print sum(truncs[4:])

