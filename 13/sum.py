#!/usr/bin/env python
import urllib2 as url
import re

numbers = [ int(i) for i in re.findall("([0-9]{50})", url.urlopen("http://projecteuler.net/problem=13").read()) ]
s = "%d" % sum(numbers)
print s[:10]
