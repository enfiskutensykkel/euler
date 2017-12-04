#!/usr/bin/env python

N = 10**6

# Calculate factors for numbers
_factors = dict([(i, None) for i in xrange(1, N + 1)])
_factors[1] = [1]

# Find prime numbers using Sieve of Eratosthenes
numbers = range(0, N+1)
for i in xrange(2, N):
	if numbers[i] != 0:
		_factors[i] = [i]
		for j in xrange(i * 2, N + 1, i):
			numbers[j] = 0

# For non-prime numbers, calculate factors
for i, factors in _factors.iteritems():
	if factors == None:
		for k in xrange(2, i / 2 + 1):
			if i % k == 0:
				_factors[i] = _factors[i / k] + [k]
				break

# Calculate number of relatively prime for n
# Euler's totient function
def phi(n, factors):
	for k in set(factors):
		n -= n / k
	return n

max_phi = 0
max_num = 0
for i in xrange(6,N+1):
	p = phi(i, _factors[i])
	r = i / float(p)

	if r > max_phi:
		max_phi = r
		max_num = i

print max_num
