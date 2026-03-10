int trova_massimo(int N, int V[]) {

    // Inserisci il tuo codice qui
    int max = V[0];

    for (int i = 1; i < N; i++) {
        if (V[i] > max) {
            max = V[i];
        }
    }

    return max;
}
