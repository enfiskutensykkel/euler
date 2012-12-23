#!/usr/bin/env python

def factorization(k):
	if k == 1:
		return [1L]

	step = 2L
	lim = k / 2L
	while step <= lim:
		if k % step == 0L:
			return factorization(k / step) + [step]

		step += 1L

	return [k]

if __name__ == '__main__':
	print int(max(factorization(600851475143L)))
