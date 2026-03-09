#!/usr/bin/env python3
# NOTE: it is recommended to use this even if you don't understand the following code.
import math

def main():
    # Read input
    line = input().split()
    N = int(line[0])
    T = int(line[1])
    K = int(line[2])
    
    a = list(map(int, input().split()))
    
    answer = -1
    
    
    # INSERT YOUR CODE HERE
    # N = numero dispositivi
    # T = minuti monitorati
    # K = lunghezza streak requisita

    min_buono = 0.67 * N
    streak = 0

    for i in range(T):

        if (a[i] >= min_buono):
            streak += 1
        else:
            streak = 0

        if streak == K:
            answer = i - K + 2
            break
    
    print(answer)
    # 10 6 3
    # 6 7 8 7 7 5

if __name__ == "__main__":
    main()
