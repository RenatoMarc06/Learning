#include <stdio.h>
void main(){
	int a, b, i, j;
	for(i=0;i<5;i++){
		printf("Digite %d par:\n",i+1);
		scanf("%d",&a);
		scanf("%d",&b);
		if(b>a){
			for(j=a+1;j<b;j++){
				if(j%2==0){
					printf("%d\n",j);
				}
			}
		}
		else if(a>b){ // Complemento
			printf("O segundo numero deve ser maior que o primeiro");
		}
}
}