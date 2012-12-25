#!/usr/bin/env python
#coding=utf8

from math import sqrt

class primes(object):

	@property
	def maximum(self):
		return len(self.numbers)


	@maximum.setter
	def maximum(self, n):
		m = len(self.numbers)
		if n > m:
			numbers = self.numbers + range(m, n)
			numbers[1] = 0

			for i in xrange(2,int(sqrt(n)+1)):
				if numbers[i]:
					for j in xrange(2*i, n, i):
						numbers[j] = 0

			self.numbers = numbers


	def __iter__(self):
		def iterator():
			step = 2
			while step < len(self.numbers):
				if self.numbers[step]:
					yield step
				step += 1

		return iterator()


	def __call__(self, n=-1):
		if n < 2:
			n = self.maximum
		elif n > self.maximum:
			self.maximum = n

		return [ p for p in iter(self) ]


	def __init__(self, n):
		self.numbers = []
		self.maximum = n if n > 2 else 2



def factorization(n):
	if n == 1:
		return [1]

	step = 2
	lim = n / 2
	while step <= lim:
		if n % step == 0:
			return factorization(n / step) + [step]

		step += 1

	return [n]


def phi(n):
	for k in set(factorization(n)):
		n -= n / k
	return n


def R(d):
	return phi(d) / (d - 1.0)



if __name__ == '__main__':
	primes = primes(30)
	target = 15499.0 / 94744.0
	step = iter(primes)

	last_prime = step.next()
	next_prime = step.next()

	d = last_prime
	f = 1

	while R(d * f) >= target:
		f += 1

		if f == next_prime:
			last_prime = next_prime
			next_prime = step.next()
			d *= f
			f = 1

	print d * f
