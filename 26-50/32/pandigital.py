#!/usr/bin/env python

def pandigital(n):
	count = {}
	for digit in str(n):
		if count.has_key(digit):
			return False

		count[digit] = True

	for i in xrange(1, len(str(n))+1):
		if not count.has_key(str(i)):
			return False

	return True



pandigits = set()
for i in xrange(2, 10):
	start = 1234

	for j in xrange(start, 10**4 / i + 1):
		if pandigital(str(i) + str(j) + str(i*j)):
			pandigits.add(i * j)

for i in xrange(10, 100):
	start = 123

	for j in xrange(start, 10**4 / i + 1):
		if pandigital(str(i) + str(j) + str(i*j)):
			pandigits.add(i * j)

print sum(pandigits)
