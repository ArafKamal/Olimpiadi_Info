#!/usr/bin/env python3
# NOTE: it is recommended to use this even if you don't understand the following code.

import sys

# uncomment the two following lines if you want to read/write from files
# sys.stdin = open('input.txt')
# sys.stdout = open('output.txt', 'w')

L, N = map(int, input().strip().split())

ans = L


# INSERT YOUR CODE HERE
# L = foglie
# N = giorni dalla piantagione

g3 = N // 3
g2 = (N // 2) - (N // 6)
g1 = N - g3 - g2

ans += g3 * 3 + g2 * 2 + g1 * 1

print(ans)

sys.stdout.close()
