#!/usr/bin/env python

numerals = {
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000
		}

values = {
		1: 'I',
		4: 'IV',
		5: 'V',
		9: 'IX',
		10: 'X',
		40: 'XL',
		50: 'L',
		90: 'XC',
		100: 'C',
		400: 'CD',
		500: 'D',
		900: 'CM',
		1000: 'M'
		}

def expand(numeral):
	i = value = 0
	while i < len(numeral):
		v = numerals[numeral[i]]

		if i < len(numeral)-1 and v < numerals[numeral[i+1]]:
			v = numerals[numeral[i+1]] - numerals[numeral[i]]
			i += 1

		i += 1
		value += v

	return value

def contract(value):
	string = ""
	remaining = value

	for v in sorted(values.keys(), reverse=True):
		while remaining >= v:
			string += values[v]
			remaining -= v

	return string

if __name__ == '__main__':
	import urllib2 as url

	saved = 0
	for line in [ line.strip() for line in url.urlopen('http://projecteuler.net/project/roman.txt').readlines() ]:
		print line, contract(expand(line))
		saved += len(line) - len(contract(expand(line)))

	print saved
