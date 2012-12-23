#!/usr/bin/env python

import urllib2 as url
import re

def search(grid, x, y):
	ranges = {
			'left': (range(0,-4,-1), [0]*4),
			'right': (range(0,4,1), [0]*4),
			'down': ([0]*4, range(0,4,1)),
			'diagl': (range(0,-4,-1), range(0,4,1)),
			'diagr': (range(0,4,1), range(0,4,1))
			}

	m = 0
	for x_r, y_r in ranges.values():
		t = 1;
		for i in xrange(0, 4):
			t *= grid[x + x_r[i]][y + y_r[i]]

		if t > m:
			m = t

	return m


if __name__ == '__main__':

	grid = [ re.findall("(?:<span.*>)?([0-9]{2})(?:<.*/span>)?", match) for match in re.findall(r"^([0-9].*)", url.urlopen("http://projecteuler.net/problem=11").read(), re.MULTILINE) ]
	grid = [ map(lambda x: int(x), i) for i in grid ]

	largest = 0
	for x in xrange(4, len(grid)-4):
		for y in xrange(0, len(grid[x])-4):
			product = search(grid, x, y)

			if product > largest:
				largest = product

	print largest
