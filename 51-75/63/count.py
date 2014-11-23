#!/usr/bin/env python
from math import ceil

# 10^(n-1) <= x^n < 10^n ==> n is positive, so lowest upper bound is 10^1, meaning that x <= 9
# if n=3, then 100 <= x^3 < 1000
# 10^(n-1) <= x^n ==> n - 1 = log(x) * n
# which gives us (n-1)/n <= log(x)
# lim n->inf (n-1)/n = 1, so 10^((n-1)/n) <= x i
# means that there is a limit where n becomes large enough for the lim to exceed x<=9

lower = 0
n = 1.0
result = 0

while lower < 10:
	lower = ceil(10**((n - 1.0) / n))
	result += 10 - lower
	n += 1.0

print result
