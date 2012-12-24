#!/usr/bin/env python
from math import sqrt

def divisors(n):
	d = [1]
	for i in xrange(2, int(sqrt(n))):
		q, r = divmod(n, i)
		if r == 0:
			d.append(q)
			d.append(i)

	return d


if __name__ == '__main__':
	amicables = {}

	for i in xrange(1, 10000):
		j = sum(divisors(i))
		if sum(divisors(j)) == i and i != j:
			amicables[i] = 1
			amicables[j] = 1

	a = amicables.keys()
	a.sort()

	print a
	print sum(a)
