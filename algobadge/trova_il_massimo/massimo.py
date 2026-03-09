#!/usr/bin/env python3
# NOTE: it is recommended to use this even if you don't understand the following code.
import math


def main():
    # Read input
    line = input().split()
    N = int(line[0])

    S = list(map(int, input().split()))

    answer = -1

    # INSERT YOUR CODE HERE
    # N = numeri totali
    # S = array di numeri

    minimo = S[0]

    for i in range (N):
        minimo = max(minimo, S[i])



    print(minimo)


if __name__ == "__main__":
    main()
