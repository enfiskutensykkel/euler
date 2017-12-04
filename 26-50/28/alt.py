#!/usr/bin/env python

# Calculate next spiral arm
def arm(r):
    return (2 * r + 1) ** 2


# Calculate short-side length of an arm
def length(r):
    if r == 0:
        return 1

    return length(r - 1) + 2


# Create spiral arm and summarise corners
def diagonal(r):
    if r == 0:
        return 1

    edge = range(arm(r - 1) + 1, arm(r) + 1)

    corner = length(r) - 2
    s = edge[corner]
    for i in range(3):
        corner += length(r) - 1
        s += edge[corner]

    return diagonal(r - 1) + s


level = 2
last = 5

while last != 1001:
    level += 1
    last = length(level)

print diagonal(level)

