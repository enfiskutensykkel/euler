#!/usr/bin/env python
import urllib2 as url
import re


numbers = [ i for i in re.findall("([0-9]{50})", url.urlopen("http://projecteuler.net/problem=8").read()) ]
number = "".join(numbers)

product = 0
for i in xrange(0,len(number)-5):
	n = int(number[i])
	for j in xrange(1,5):
		n *= int(number[i+j])

	if n > product:
		product = n

print product
