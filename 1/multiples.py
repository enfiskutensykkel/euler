#!/usr/bin/env python

print "%d" % sum(map(lambda x: x if x % 5 == 0 or x % 3 == 0 else 0, range(3, 1000)))
