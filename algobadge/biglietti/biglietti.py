#!/usr/bin/env python3
import math


def main():
    # Read input
    fr = open("input.txt", "r")
    fw = open("output.txt", "w")

    line = fr.readline().split()
    N = int(line[0])
    M = int(line[1])
    A = int(line[2])
    B = int(line[3])

    answer = -1

    # N = numero di viaggi che deve fare
    # M = numero viaggi in abbonamento
    # A = prezzo in centesimi
    # B = prezzo abbonamento

    costoM = M * A

    if (costoM <= B):
        answer = N * A
    else:
        answer = (N // M) * B + min((N % M) * A, B)

    fw.write(str(answer) + "\n")

    fr.close()
    fw.close()

    return 0


if __name__ == "__main__":
    main()