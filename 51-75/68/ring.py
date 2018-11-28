#!/usr/bin/env python

def solution(ring):
    n = len(ring) / 2

    arms = []
    total = None
    lowest = n
    for pos in range(n + 1, 2 * n):
        if ring[pos] < ring[lowest]:
            lowest = pos

    for i in range(n):
        pos = ((lowest + i) % n) + n
        arm = (ring[pos], ring[pos - n], ring[(pos - n + 1) % n])
        arms.append(arm)

    return tuple(arms)


def add_rings(n, target, pos, rings, current):
    if pos == 2 * n:
        s = solution(current)
        if not s in rings:
            rings.append(s)
        return

    numbers = filter(lambda x: not x in current, range(1, 2 * n + 1))
    for number in numbers:
        if pos >= n and (number + current[pos - n] + current[(pos - n + 1) % n]) != target:
            continue

        current[pos] = number
        add_rings(n, target, pos + 1, rings, current)
        current[pos] = None


def rings(n):
    numbers = range(1, 2*n + 1)
    minimum = numbers[0] + numbers[1] + numbers[2]
    maximum = numbers[-3] + numbers[-2] + numbers[-1]

    rings = []
    for target in range(minimum, maximum + 1):
        add_rings(n, target, 0, rings, [None for i in numbers])

    return rings


def string(ring):
    s = ""
    for arm in ring:
        for number in arm:
            s += str(number)

    return s


m = 0
for ring in rings(5):
    s = string(ring)
    n = int(s)
    if len(s) == 16 and n > m:
        m = n

print m
