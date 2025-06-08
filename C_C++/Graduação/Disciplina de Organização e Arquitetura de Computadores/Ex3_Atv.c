#include <stdio.h>
void main(){	
int Naluno;
float Haluno;
int i;
int NumMaior = 0, NumMenor = 0;
float Maior = 0,Menor = 0;

	for(i=0;i<10;i++){
		printf("Digite o numero do aluno: ");
		scanf("%d",&Naluno);
		
		printf("Digite a altura do aluno: (cm)\n");
		scanf("%f",&Haluno);
		
		if(Maior<Haluno){
			Maior = Haluno;
			NumMaior = Naluno;
		}
		if(Menor == 0 || Menor>Haluno){
			Menor = Haluno;
			NumMenor = Naluno;
		}
		
}
	printf("O maior aluno e o numero %d com a altura de %.2fcm\n",NumMaior,Maior);
	printf("O menor aluno e o numero %d com a altura de %.2fcm",NumMenor,Menor);
}