#!/usr/bin/env python3
# NOTE: it is recommended to use this even if you don't understand the following code.

import sys

# uncomment the two following lines if you want to read/write from files
sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

lo, hi, pos = map(int, input().strip().split())

pressedButtons = input().strip()

ans = pos


# INSERT YOUR CODE HERE

# lo = posizione più bassa
# hi = posizione più alta
# pos = posizione corrente
# "error" se non esiste

for c in pressedButtons:
    if c == "U":
        ans += 1
    elif c == "D":
        ans -= 1
    elif c == "0":
        ans = 0

    if ans < lo or ans > hi:
        ans = "error"
        break

print(ans)

sys.stdout.close()
