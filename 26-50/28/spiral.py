#!/usr/bin/env python

#  1
#  3,  5,  7,  9 | 2
# 13, 17, 21, 25 | 4
# 31, 37, 43, 49 | 6
def edges(n):
	if n == 1:
		return [1]

	edge = edges(n-2)
	return edge + [ i for i in range(edge[-1]+(n-1), edge[-1]+5*(n-1), n-1) ]

print sum(edges(1001))
