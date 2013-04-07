#!/usr/bin/env python

# This one is really simple because of the constraints given:
# 1) Fraction is less than one, in other words numerator < denominator.
# 2) There are two digits in nominator and denominator, meaning that x and y
#    are between 10 and 99, this gives us 90 * 90 different possibilities to
#    check.
# 3) All fractions x/y where x is divisible by 10 is discarded as trivial.

from __future__ import division
from fractions import gcd


def cancel(x, y):
	xdigits = str(x)
	ydigits = str(y)

	any_left = True
	while any_left:
		any_left = False

		for xpos, xdig in enumerate(str(xdigits)):
			if any_left: break

			for ypos, ydig in enumerate(str(ydigits)):
				if any_left: break

				if xdig == ydig:
					any_left = True
					xdigits = xdigits[0:xpos] + xdigits[xpos+1:]
					ydigits = ydigits[0:ypos] + ydigits[ypos+1:]

	if len(xdigits) == 0 or len(ydigits) == 0 or int(ydigits) == 0:
		return x, y
	else:
		return int(xdigits), int(ydigits)


frac = (1, 1)
for x in xrange(10, 100):
	for y in xrange(x+1, 100):
		x_m, y_m = cancel(x, y)

		if x != x_m and y != y_m and x % 10 != 0 and x / y == x_m / y_m:
			frac = (frac[0] * (x_m), frac[1] * (y_m))

print frac[1] / gcd(frac[0], frac[1])
