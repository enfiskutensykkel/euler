#!/usr/bin/env python

# We have the following two equations
# (1) a^2 + b^2 = c^2
# (2) a + b + c = p    => c = p - a - b

# Using those, we know that
# b = (p^2 - 2ap) / (2p - 2a)
# Since we're only interested in integral sides, we kan simply check modulus

# Also, since a^2 + b^2 = c^2, we know that a <= b < c
# which again means that a + b + c = p  =>  a <= p/3


solutions = {}
for p in xrange(2, 1001):
	solutions[p] = 0
	for a in xrange(2, p / 3):
		if (p**2 - 2*p*a) % (2*p - 2*a) == 0:
			solutions[p] += 1

print reduce(lambda x, y: x if solutions[x] > solutions[y] else y, solutions.keys())
