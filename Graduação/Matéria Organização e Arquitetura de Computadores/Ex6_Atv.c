#include <stdio.h>
void main(){
	int i,j = 0,n,Num,Soma = 0, SomaPar = 0,Maior = -2147483647, Menor = 2147483647; // Maior int permitido
	float Media, MediaPar;
	printf("Digite a quantidade de numeros a serem recebidos: ");
	scanf("%d",&n);
	if (n<0){
		n = n*(-1);
	}
	for(i=0;i<n;i++){
		printf("Digite numero %d: ",i+1);
		scanf("%d",&Num);
		if(Maior<Num){
			Maior = Num;
		}
		if(Menor>Num){
			Menor = Num;
		}
		Soma = Soma + Num;
		
		if(Num%2==0){
			SomaPar = SomaPar + Num;
			j++;
		}
		
	}
	Media = Soma/n;
	//Soma
	printf("A soma e: %d\n", Soma);
	//Quantidade de numeros
	printf("A quantidade de numeros e: %d\n", n);
	//Media
	printf("A media e: %.2f\n", Media);	
	//Maior numero
	printf("A maior numero e: %d\n", Maior);	
	//Menor numero
	printf("A menor numero e: %d\n", Menor);
	//Media de numero pares
	if(j==0){
		printf("Nao ha numeros pares\n");
	}
	else{
		MediaPar = SomaPar/j;
		printf("A media dos numeros pares e: %.2f\n",MediaPar);
	}
	//Porcentagem de impares
	float PercImpar = ((float)(n - j) / n) * 100;
		printf("A porcentagem de numero impares e: %.2f\n",PercImpar);
}