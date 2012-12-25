#!/usr/bin/env python
#coding=utf8

# I've solved this by creating a tree like structure
# where every element in the matrix is a tree node with
# two children.
#
# I then run Dijkstra's algorithm on it to compute the
# shortest path. Obviously this isn't the most efficient
# algorithm, but it runs to completion in less than 4 mins,
# so it can't be that bad, can it?

class node(object):
	def __init__(self, value):
		self.val = value
		self.down = None
		self.right = None

	def __str__(self):
		return str(self.val)

	@staticmethod
	def dijkstra(matrix, source):
		infinity = 2147483646
		graph = []
		for x in xrange(0, len(matrix)):
			for y in xrange(0, len(matrix[x])):
				graph.append(matrix[x][y])

		dist = {}
		prev = {}
		Q = []
		for v in graph:
			dist[v] = infinity
			Q.append(v)
			prev[v] = None

		dist[source] = source.val

		while len(Q) > 0:
			Q.sort(cmp=lambda v, w: dist[v] < dist[w])
			u = Q[0]; Q = Q[1:]

			if dist[u] == infinity:
				break

			for v in [u.down, u.right]:
				if v == None:
					continue

				alt = dist[u] + v.val
				if alt < dist[v]:
					dist[v] = alt
					prev[v] = u

		return dist

	@staticmethod
	def create_tree(matrix):

		for x in xrange(0, len(matrix)):
			for y in xrange(1, len(matrix[x])):
				matrix[x][y-1].right = matrix[x][y]

		for x in xrange(1, len(matrix)):
			for y in xrange(0, len(matrix[x])):
				matrix[x-1][y].down = matrix[x][y]



if __name__ == '__main__':
	import urllib2
	#matrix = [ [ node(int(d)) for d in line.split(",") ] for line in open("matrix.txt").readlines() ]
	matrix = [ [ node(int(d)) for d in line.split(",") ] for line in urllib2.urlopen('http://projecteuler.net/project/matrix.txt').readlines() ]

	node.create_tree(matrix)
	print node.dijkstra(matrix, matrix[0][0])[matrix[79][79]]
