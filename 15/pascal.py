#!/usr/bin/env python

def pascal(n):
	triangle = [[1], [1,1]]
	for i in xrange(2,n):
		row = []
		for j in xrange(1, len(triangle[i-1])):
			row.append(triangle[i-1][j-1] + triangle[i-1][j])
		triangle.append([1] + row + [1])

	return triangle

def grid(dim):
	tri = pascal(2*dim+1)
	return tri[2*dim][dim]

print grid(20)
