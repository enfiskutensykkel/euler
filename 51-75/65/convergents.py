#!/usr/bin/env python

# 1,2,1, 1,4,1, 1,6,1, ...
def sequence(k, n):
	while k < n:
		yield 2 * (k/3 + 1) if k % 3 != 0 and (k+1) % 3 != 0 else 1
		k += 1


# rationalize the fraction
def rationalize(f):
	if len(f) == 1:
		return (f[0], 1)

	n, d = rationalize(f[1:])

	return (f[0] * n + d, n)


e = [2] + [k for k in sequence(0, 99)]
print sum(int(d) for d in str(rationalize(e)[0]))
