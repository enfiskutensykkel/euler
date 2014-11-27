#!/usr/bin/env python

cubes = {}

for i in xrange(1, 10**4):
	x = i ** 3
	s = str(sorted(str(x)))

	if not s in cubes:
		cubes[s] = []
	cubes[s].append(x)

fives = []

for k, v in cubes.iteritems():
	if len(v) == 5:
		fives.append(min(v))

print min(fives)
