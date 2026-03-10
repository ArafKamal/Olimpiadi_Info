#include <stdio.h>

int main() {
    FILE *fr = fopen("input.txt", "r");
    FILE *fw = fopen("output.txt", "w");

    // ===== LETTURA INPUT =====
    int N;
    fscanf(fr, "%d", &N);

    int a, b;
    int max_pari = -1;

    // ===== CICLO SULLE COPPIE =====
    for(int i = 0; i < N; i++) {
        fscanf(fr, "%d %d", &a, &b);

        int s = a + b;

        if (s % 2 == 0) {
            if (s > max_pari) {
                max_pari = s;
            }
        }
    }


    fprintf(fw, "%d\n", max_pari);

    fclose(fr);
    fclose(fw);
    return 0;
}