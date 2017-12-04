#!/usr/bin/env python

def continued(S):
	# Algorithm taken from http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
	m = 0
	d = 1
	a = a0 = int((S ** .5) // 1) # S ^ 1/2 = square root of S

	while 1:
		m = d * a - m
		d = (S - m**2) / d
		a = (a0 + m) // d

		yield m, d, a

# Pell's equation x^2 - Dy^2 = 1 --> x^2 = Dy^2 + 1
# (p, q) is a minimal solution if p/q is a convergent of sqrt(D)
# http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Pell.27s_equation
def Pell(D):
	cont = continued(D)

	p_prev = 1
	p_curr = int((D ** .5) // 1)
	q_prev = 0
	q_curr = 1
	p_next = q_next = 0

	while 1:
		m, d, a = next(cont)
		p_next = int(a) * p_curr + p_prev
		q_next = int(a) * q_curr + q_prev

		if p_next * p_next - D * q_next * q_next == 1:
			return p_next, q_next

		p_prev = p_curr
		p_curr = p_next

		q_prev = q_curr
		q_curr = q_next

if __name__ == '__main__':
	x_max = 0
	D_max = 0

	for D in xrange(1001):
		lim = D ** .5 // 1
		if lim * lim == D:
			continue

		x, y = Pell(D)

		if x > x_max:
			x_max = x
			D_max = D

	print x_max
	print D_max
