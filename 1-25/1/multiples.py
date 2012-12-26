#!/usr/bin/env python

print sum(x for x in range(3, 1000) if x % 5 == 0 or x % 3 == 0)
