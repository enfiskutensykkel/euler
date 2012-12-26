#!/usr/bin/env python

class node(object):
	def __init__(self, value):
		self.value = value
		self.children = []
		self.visited = False

	def add_child(self, node):
		if not node in self.children:
			self.children.append(node)

	def traverse(self, path):
		path.append(self)

		for child in self.children:
			child.traverse(path)

	def __repr__(self):
		return self.value

	def remove_links(self):
		keep = [ child for child in self.children ]
		remove = []

		for child in self.children:
			for grandchild in child.children:
				path = []
				grandchild.traverse(path)

				for node in keep:
					if node in path:
						keep.remove(node)
						remove.append(node)

		for child in remove:
			self.children.remove(child)


if __name__ == '__main__':
	import urllib2 as url

	graph = {}

	# build graph
	for digits in [ line.strip() for line in url.urlopen('http://projecteuler.net/project/keylog.txt').readlines() ]:
		for position, digit in enumerate(digits): # just learned about this
			if not graph.has_key(digit):
				graph[digit] = node(digit)

			if position > 0:
				graph[digits[position-1]].add_child(graph[digit])

	# remove links (build tree)
	for node in graph.values():
		node.remove_links()

	# find root
	has_parents = []
	for node in graph.values():
		has_parents += node.children

	# print tree
	for node in graph.values():
		if node not in has_parents:
			path = []
			node.traverse(path)
			print "".join([ v.value for v in path])
