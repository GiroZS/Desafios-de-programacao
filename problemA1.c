#include <stdio.h>
#include <string.h>

int main(){
    int n;
    char s[5001];  // Aumentamos o tamanho para 5001 (5000 + 1 para o caractere nulo)

    // Lê o valor de 'n' e a string 's'
    scanf("%d\n%s", &n, s);
    int l;

    // Percorre a string comparando caracteres a 'N' posições uns dos outros
    for (int i = 1; i < n; i++) {
        l = 0;

        // Verifica o maior l tal que S[k] != S[k+i] para todos os k
        while (l + i < n && s[l] != s[l + i]) {
            l++;
        }

        // Imprime o valor máximo de l encontrado para este i
        printf("%d\n", l);
    }

    return 0;
}
