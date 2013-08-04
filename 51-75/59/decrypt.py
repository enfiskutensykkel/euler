#!/usr/bin/env python

def most_common(l):
	common = {}

	for item in l:
		common[item] = (common[item] + 1) if item in common else 1

	most = None
	for item, count in common.iteritems():
		if most is None or count > common[most]:
			most = item

	return most


if __name__ == '__main__':
	import urllib2 as url

	encrypted = [int(c) for c in url.urlopen('http://projecteuler.net/project/cipher1.txt').read().split(',')]

	# we know that the key is 3 letters only
	piles = []
	piles.append(encrypted[0::3])
	piles.append(encrypted[1::3])
	piles.append(encrypted[2::3])

	# find most common character and assume it's a space
	keys = []
	for pile in piles:
		keys.append(most_common(pile) + ord(' '))

	# decrypt using the keys
	decrypted = ""
	for pos, char in enumerate(encrypted):
		decrypted += chr(char ^ keys[pos % 3])

	print decrypted
	print sum([ord(c) for c in decrypted])

