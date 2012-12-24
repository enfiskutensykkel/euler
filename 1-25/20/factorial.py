#!/usr/bin/env python

def fac(n, acc=1):
	if n == 0:
		return acc

	# Not that tail-recursion is going to help us here anyway
	# since Python can't do that stuff
	return fac(n-1, n*acc)


print reduce(lambda x, y: int(x) + int(y), str(fac(100)))
