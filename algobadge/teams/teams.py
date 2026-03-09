#!/usr/bin/env python3
# NOTE: it is recommended to use this even if you don't understand the following code.

import sys

# uncomment the two following lines if you want to read/write from files
# sys.stdin = open('input.txt')
# sys.stdout = open('output.txt', 'w')

A = int(input().strip())

B = int(input().strip())

T = 42


# INSERT YOUR CODE HERE
T = teams = min(A, B, (A + B) // 4)

print(T)

sys.stdout.close()
