#include <stdio.h>

int main() {
    FILE *fr = fopen("input.txt", "r");
    FILE *fw = fopen("output.txt", "w");

    int N;
    fscanf(fr, "%d", &N);
    int S[N];

    for(int i = 0; i < N; i++) {
        fscanf(fr, "%d", &S[i]);
    }

    int max = S[0];

    // codice qua
    for (int i = 1; i < N; i++) {
        if (S[i] > max) {
            max = S[i];
        }
    }

    fprintf(fw, "%d\n", max);

    fclose(fr);
    fclose(fw);
}