#!/usr/bin/env python
#coding=utf8

wordmap = {
		0: '',
		1: 'one',
		2: 'two',
		3: 'three',
		4: 'four',
		5: 'five',
		6: 'six',
		7: 'seven',
		8: 'eight',
		9: 'nine',
		10: 'ten',
		11: 'eleven',
		12: 'twelve',
		13: 'thirteen',
		14: 'fourteen',
		15: 'fifteen',
		16: 'sixteen',
		17: 'seventeen',
		18: 'eighteen',
		19: 'nineteen',
		20: 'twenty',
		30: 'thirty',
		40: 'fourty',
		50: 'fifty',
		60: 'sixty',
		70: 'seventy',
		80: 'eighty',
		90: 'ninety',
		100: 'onehundred',
		200: 'twohundred',
		300: 'threehundred',
		400: 'fourhundred',
		500: 'fivehundred',
		600: 'sixhundred',
		700: 'sevenhundred',
		800: 'eighthundred',
		900: 'ninehundred',
		1000: 'onethousand'
}

def createstr(n):
	string = wordmap[n % 100]
	if n >= 1000:
		string = wordmap[1000]
	elif n >= 100:
		string = wordmap[n / 100 * 100] + ("and" if n % 100 != 0 else "") + string
	return string

for i in range(20,100,10):
	for j in range(1,10):
		wordmap[i+j] = wordmap[i] + wordmap[j]


wc = 0
for i in range(1,1001):
	s = createstr(i)
	print s
	wc += len(s)
print wc

