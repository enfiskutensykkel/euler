#!/usr/bin/env python

#m = 0
#for a in xrange(1, 100):
#	for b in xrange(1, 100):
#		n = sum([ int(x) for x in str(a**b) ])
#		if n > m:
#			m = n

print max([ max([ sum([int(x) for x in str(a**b) ]) for a in xrange(1,100) ]) for b in xrange(1,100) ])
