#!/usr/bin/env python


n = 9
while 1:
	lim = sum(int(d)**5 for d in str(n))
	if len(str(lim)) < len(str(n*10+9)):
		break
	n = 10*n + 9

powers = set()
for x in xrange(2, lim):
	if sum(int(d)**5 for d in str(x)) == x:
		powers.add(x)

print powers
print sum(powers)
