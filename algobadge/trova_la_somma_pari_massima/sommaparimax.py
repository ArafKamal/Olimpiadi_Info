#!/usr/bin/env python3

def main():
    fr = open("input.txt", "r")
    fw = open("output.txt", "w")

    N = int(fr.readline())
    massimo = -1

    for _ in range(N):
        a, b = map(int, fr.readline().split())
        s = a + b

        if s % 2 == 0:
            massimo = max(massimo, s)

    fw.write(str(massimo) + "\n")

    fr.close()
    fw.close()

if __name__ == "__main__":
    main()