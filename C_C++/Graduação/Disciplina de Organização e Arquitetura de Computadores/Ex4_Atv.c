#include <stdio.h>
void main(){
	int i;
	int ant = 0, atual = 1, prox;

	for (i = 0; i < 8; i++) {
		printf("%d\n", ant);
        prox = ant + atual;
        ant = atual;
        atual = prox;
}
    printf("\n");
}
