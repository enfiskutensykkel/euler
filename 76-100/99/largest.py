#!/usr/bin/env python
from math import log

with open("p099_base_exp.txt") as handle:
	numbers = []
	for line in handle.readlines():
		base, exponent = line.split(",")
		numbers.append((int(base), int(exponent)))

# log(a^b) = b*log(a)

max_i = 0
m_base, m_exp = numbers[0]
m_log = m_exp * log(m_base)

for i in xrange(1, len(numbers)):
	base, exp = numbers[i]
	i_log = exp * log(base)

	# Check if greater
	if m_log / i_log < 1.0:
		max_i = i
		m_log = i_log

# Result is line number (lines start at 1)
print max_i + 1
