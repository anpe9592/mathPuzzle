#! /usr/bin/python3

import itertools

z = 0

for a, b, c, d, e, f, g, h, i in itertools.permutations(range(1, 10)):
    if round (a + 13 * b / c + d + 12 * e - f - 11 + g * h / i - 10, 10) == 66:
        print(a, b, c, d, e, f, g, h, i)
        z += 1

print(z, "solutions found")
