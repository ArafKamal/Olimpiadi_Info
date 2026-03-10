cmake_minimum_required(VERSION 4.1)
project(Olimpiadi_Info C)

set(CMAKE_C_STANDARD 11)

add_executable(Olimpiadi_Info
        algobadge/trova_il_massimo/massimo.c
        algobadge/trova_la_somma_pari_massima/sommaparimax.c
        algobadge/massimo2/massimo.c
        algobadge/massimo2/grader.c
        "algobadge/rsa/grader (1).c"
        algobadge/rsa/rsa.c)
