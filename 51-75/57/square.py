#!/usr/bin/env python

# 3  7  17  41  99  239 => num(n) = num(n-1) + 2 * den(n-1)
# 2  5  12  29  70  169 => den(n) = num(n) - den(n-1)

den = 2
num = 3

n = 0
for i in xrange(0, 1000):
	num += 2 * den
	den = num - den
	n += len(str(num)) > len(str(den))

print n
