#!/usr/bin/env python
print reduce(lambda x, y: int(x) + int(y), str(2**1000))
