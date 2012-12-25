#!/usr/bin/env python

def triangle(n):
	return n/float(2) * (n + 1)

def score(s):
	score = 0.0
	for c in s[1:-1]:
		score += ord(c) - ord('A') + 1
	return score

if __name__ == "__main__":
	import urllib2
	#words = open("words.txt").read().split(',')
	words = urllib2.urlopen("http://projecteuler.net/project/words.txt").read().split(',')

	t = []
	for j in range(1,21):
		t.append(triangle(j))

	triangles = 0
	for word in words:
		i = score(word)

		if i in t:
			triangles += 1

	print triangles
