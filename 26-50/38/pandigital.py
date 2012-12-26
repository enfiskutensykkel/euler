#!/usr/bin/env python

def pandigital(n):
	count = [0] * (len(str(n)) + 1)
	count[0] = 1

	for digit in str(n):
		count[int(digit)] += 1

	for i in count:
		if i != 1:
			return False

	return True

largest = 918273645
for i in xrange(2, 10**5):
	j = 1

	n = ""
	while len(n) < 9:
		n += str(i * j)
		j += 1

	if pandigital(n) and int(n) > largest:
		largest = int(n)
		print n
