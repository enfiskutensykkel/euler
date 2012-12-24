#!/usr/bin/env python

fib = [1, 1, 0]
idx = 0
sum = 0

while fib[idx] + fib[(idx-1)%3] < 4*10**6:
	fib[(idx+1) % 3] = fib[idx] + fib[(idx-1) % 3]
	idx = (idx + 1) % 3
	if fib[idx] % 2 == 0:
		sum += fib[idx]

print sum
