#!/usr/bin/env python

# Not very efficient, but small number so we can bruteforce it easily
largest = 0
for i in xrange(100, 1000):
	for j in xrange(100, 1000):
		x = i * j
		if str(x)[::-1] == str(x) and x > largest:
			largest = x

print largest
