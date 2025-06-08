#include <stdio.h>
void main(){
	int i,j=0,CodigoC, NumPasseio, NumAcidentes;
	int MaiorAcidentes = 0, MenorAcidentes = 0, CodigoMaior, CodigoMenor;
	float Soma = 0, SomaC = 0;
	for(i=0;i<5;i++){
		
 	   printf("Digite o codigo da cidade: ");
 	   scanf("%d",&CodigoC);
 	   printf("Digite o numero de veiculos de passeio da cidade: ");
 	   scanf("%d",&NumPasseio);
   	   printf("Digite o numero de acidentes de transito da cidade: ");
 	   scanf("%d",&NumAcidentes);
 	   
 	   if(MaiorAcidentes<NumAcidentes){
			MaiorAcidentes = NumAcidentes;
			CodigoMaior = CodigoC;
		}
		if(MenorAcidentes == 0 || MenorAcidentes > NumAcidentes){
			MenorAcidentes = NumAcidentes;
			CodigoMenor = CodigoC;
		}
		
		Soma = Soma + NumPasseio;
		
		if(NumPasseio<2000){
			SomaC = SomaC + NumAcidentes;
			j++;
		}

}
	// a)
	printf("A cidade %d possui o maior numero de acidentes: %d\n",CodigoMaior, MaiorAcidentes);
	printf("A cidade %d possui o menor numero de acidentes: %d\n",CodigoMenor, MenorAcidentes);
	// b)
	printf("A media de veiculos nas 5 cidades e: %.2f\n",Soma/5);
	// c)
	if(j == 0){
		printf("Nenhuma cidade possui menos de 2000 veiculos");
	}
	else{
	   	printf("A media de acidentes nas cidades com menos de 2000 veiculos de passeio e: %.2f\n",SomaC/j);
	}	   
}