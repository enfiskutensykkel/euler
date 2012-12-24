#!/usr/bin/env python

print sum(xrange(1,101))**2 - sum(map(lambda x: x**2, range(1,101)))
