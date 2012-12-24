#!/usr/bin/env python
import re, urllib2 as url

def score(name):
	score = 0
	for c in name[1:-1]:
		score += ord(c) - ord('A') + 1
	return score

if __name__ == "__main__":
	#names = open("names.txt").read().split(',')
	names = url.urlopen("http://projecteuler.net/project/names.txt").read().split(',')
	names.sort()

	s = 0
	for i in xrange(0,len(names)):
		s += score(names[i]) * (i+1)

	print s

