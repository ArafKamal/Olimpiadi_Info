#!/usr/bin/env python3
import sys
import math

sys.stdin = open(r"C:\Users\14530113\Olimpiadi_Info\algobadge\caramelle\caramelle_input_1.txt")
sys.stdout = open("output.txt", "w")

def read_int():
    while True:
        line = input()
        if line.strip() != "":
            return int(line)

def read_list():
    while True:
        line = input()
        if line.strip() != "":
            return list(map(int, line.split()))

T = read_int()

for test in range(1, T + 1):
    N = read_int()
    V = read_list()

    # codice 

    c = 1
    for elemento in V:
        c = c * elemento // math.gcd(c, elemento)

    print(f"Case #{test}: {c}")

sys.stdout.close()
