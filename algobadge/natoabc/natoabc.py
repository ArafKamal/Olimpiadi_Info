#!/usr/bin/env python3
# NOTE: it is recommended to use this even if you don't understand the following code.

import sys

# uncomment the two following lines if you want to read/write from files
sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

S = input().strip()

T = ""



# INSERT YOUR CODE HERE
mappa = {
    "alpha":"a", "bravo":"b", "charlie":"c", "delta":"d", "echo":"e", "foxtrot":"f",
    "golf":"g", "hotel":"h", "india":"i", "juliett":"j", "kilo":"k", "lima":"l",
    "mike":"m", "november":"n", "oscar":"o", "papa":"p", "quebec":"q", "romeo":"r",
    "sierra":"s", "tango":"t", "uniform":"u", "victor":"v", "whiskey":"w", "xray":"x",
    "yankee":"y", "zulu":"z"
}

i = 0
while i < len(S):
    for parola, lettera in mappa.items():
        if S.startswith(parola, i):
            T += lettera
            i += len(parola)
            break



print(T)

sys.stdout.close()
