#!/usr/bin/env python3
# NOTE: it is recommended to use this even if you don't understand the following code.

import sys

# uncomment the two following lines if you want to read/write from files
sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

N = int(input().strip())

F = [0 for i in range(N)]
T = ['-' for i in range(N)]
for i in range(N):
    F[i], T[i] = [f(v) for f, v in zip([int, str], input().strip().split())]

K = 0


# INSERT YOUR CODE HERE
# N = numero di volte mangiare (0, N-1)
# quando cibo, F[i] grammi, T[i] tipo di cibo
# T[i] = M o B

# per cambiare pannolino,
# piscio: 50 grammi M
# cacca: 80 grammi B

latte = 0
cibo = 0

for i in range(N):
    if (latte >= 50 or cibo >= 80):
        K += 1
        if (latte >= 50):
            latte -= 50
        else:
            cibo -= 80

    if (T[i] == "M"):
        latte += F[i]
    else:
        cibo += F[i]

print(K)

sys.stdout.close()
