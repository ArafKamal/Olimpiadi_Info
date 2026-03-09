#!/usr/bin/env python3

def main():
    fr = open("input.txt", "r")
    fw = open("output.txt", "w")

    # ===== LETTURA INPUT =====
    # esempio lettura
    N = int(fr.readline())
    ris = 0

    # ===== SCRIVI QUI IL TUO CODICE =====

    ris = N * (N-1) / 4

    # ===== SCRITTURA OUTPUT =====
    # esempio
    fw.write(str(ris) + "\n")

    fr.close()
    fw.close()


if __name__ == "__main__":
    main()