#!/usr/bin/env python

from math import sqrt

def divisors(n):
	divs = []
	for i in xrange(1, int(sqrt(n))+1):
		if n % i == 0:
			divs.append(i)
			divs.append(n/i)

	return divs

def triangle():
	i, n = 7, 28 # from the problem page

	while 1:
		yield n
		i += 1
		n += i


if __name__ == '__main__':
	iterator = triangle()
	num_divs = 0

	for t in iterator:
		divs = len(divisors(t))

		if divs > num_divs:
			num_divs = divs
			print t, divs

			if divs >= 500:
				break
