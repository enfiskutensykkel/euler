#!/usr/bin/env python

def continuants(S):
	m = 0
	d = 1
	a = a0 = int((S ** .5) // 1)

	p_p = 1
	p_n = a0
	q_p = 0
	q_n = 1

	while True:
		m = d * a - m
		d = (S - m * m) / d
		a = (a0 + m) // d

		p = a * p_n + p_p
		q = a * q_n + q_p

		yield p, q

		p_p = p_n
		q_p = q_n
		p_n = p
		q_n = q

def div(a, b, n):
	times = a // b
	remainder = a - b * times

	digits = str(times)

	if remainder != 0 and n > 0:
		digits += div(remainder * 10, b, n - 1)

	return digits


def sqrt(n):
	sqrt_gen = continuants(n)

	# arbitrary chosen precission, should probably have calculated this
	for i in xrange(200):
		next(sqrt_gen)
	p, q = next(sqrt_gen)

	s = div(p, q, 100)
	return s[:100]

def issquare(x):
	sqrt_x = x ** .5
	return sqrt_x == sqrt_x // 1


if __name__ == '__main__':
	total = 0
	for x in xrange(1, 101):
		if not issquare(x):
			total += sum(int(c) for c in sqrt(x))

	print total

