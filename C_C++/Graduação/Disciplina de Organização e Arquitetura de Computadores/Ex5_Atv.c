#include <stdio.h>
void main(){
	int Idade, i, j;
	float Peso, Altura;
	int Menor18 = 0;
	float SomaIdade, MediaIdade;
	float SomaAltura = 0;
	int Mais80 = 0;
	
	for(i=0;i<5;i++){
		SomaIdade = 0;
		for(j=0;j<11;j++){
			printf("Digite a idade do jogador: ");
			scanf("%d", &Idade);
			printf("Digite o peso do jogador: ");
			scanf("%f", &Peso);
			printf("Digite a altura do jogador: ");
			scanf("%f", &Altura);
			
			if(Idade<18){
				Menor18++;
			}
			
			if(Peso>80){
				Mais80++;
			}
			
			SomaIdade += Idade;
			SomaAltura += Altura;
		}
		//Media da idade dos jogadores de cada time
		MediaIdade = SomaIdade/11;
		printf("Media de idade do time %d: %.2f\n", i+1, MediaIdade);
	}
	//Jogadores com menos de 18
	printf("Quantidade de jogadores com menos de 18 anos: %d\n", Menor18);
	//Media da altura de todos os times
	printf("Media de altura de todos os jogadores: %.2f\n", SomaAltura/55);
	//Percentual de jogadores com mais de 80kgs
	printf("Percentagem de jogadores com mais de 80kg: %.2f%%\n", (Mais80*100.0)/55);
}