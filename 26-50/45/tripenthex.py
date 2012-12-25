#!/usr/bin/env python

def T(n):
	return (n * (n+1)) / 2

def P(n):
	return (n * (3*n - 1)) / 2

def H(n):
	return n * (2*n - 1)

def mpos(n):
	m = 0
	equal = True

	for i in xrange(1, len(n)):

		if n[i] != n[m]:
			equal = False

			if n[i] < n[m]:
				m = i

	return m if not equal else -1


i = [ 286, 165, 143 ]
j = [ T(i[0]), P(i[1]), H(i[2]) ]
f = [ T, P, H ]

while mpos(j) != -1:
	k = mpos(j)
	i[k] += 1
	j[k] = f[k](i[k])

print i
print j
