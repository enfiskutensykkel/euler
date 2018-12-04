#!/usr/bin/env python

# Criterias:
# 1: a < b < c
# 2: a^2 + b^2 = c^2
# 3: a + b + c = 1000


x = 1000

for a in range(1, x):
    for b in range(a + 1, x / 2):
        y = a + b + (a**2 + b**2) ** .5 # 1000 = a + b + sqrt(a^2 + b^2)
        if y == 1000:
            c = 1000 - a - b
            print a * b * c
