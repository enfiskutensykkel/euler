#!/usr/bin/env python

def merge(tri):
	for i in xrange(len(tri)-2, -1, -1):
		for j in xrange(0, len(tri[i]), 1):
			tri[i][j] += max(tri[i+1][j], tri[i+1][j+1])

	return tri[0][0]


if __name__ == '__main__':
	import re, urllib2 as url

	triangle = []
	#for line in open("triangle.txt").readlines():
	for line in url.urlopen("http://projecteuler.net/project/triangle.txt").readlines():
		row = re.findall("([0-9]+)", line)
		triangle.append([ int(x) for x in row ])


	print merge(triangle)

