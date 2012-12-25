#!/usr/bin/env python

def rot(s):
	t = []; s = str(s)
	for i in xrange(0, len(s)):
		t.append(int(s[i:] + s[0:i]))

	return t


same = 0
x = 0
while not same:
	x += 1
	var = rot(x)

	same = 1
	for y in xrange(2,7):
		if not y*x in var:
			same = 0
			break

print x

