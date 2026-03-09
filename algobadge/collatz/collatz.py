#!/usr/bin/env python3

def main():
    fr = open("input.txt", "r")
    fw = open("output.txt", "w")

    # ===== LETTURA INPUT =====
    # esempio lettura
    N = int(fr.readline())

    # ===== SCRIVI QUI IL TUO CODICE =====

    L = 1

    while N != 1:
        if N % 2 == 0:
            N /= 2
        else:
            N *= 3
            N += 1
        
        L += 1

    # ===== SCRITTURA OUTPUT =====
    # esempio
    fw.write(str(L) + "\n")

    fr.close()
    fw.close()


if __name__ == "__main__":
    main()