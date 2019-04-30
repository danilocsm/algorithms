#include <stdio.h>
#include <stdlib.h>

int binary_search(int *vet,int elm,int size)
{
	int end,beg,meio;

	beg = 0;
	end = size-1;
	meio = (end+beg)/2;

	while(meio>=beg && meio<=end){

		if(elm > vet[meio]){
			beg = meio+1;
			meio = (beg+end)/2;
		}
		else if(elm < vet[meio]){
			end = meio - 1;
			meio = (beg+end)/2;
		}
		else{
			
			if(meio==0)
				return meio;	
			else if(vet[meio-1] == elm){
				end = meio-1;
				meio = (beg+end)/2;
			}
			else
				return meio;
		}
	}

	return -1;

}


int particiona(int *vet,int beg,int end)
{
	int pivo=vet[beg];
	int i=beg+1,f=end;

	while(i<=f){
		if(vet[i]<=pivo)							
			i++;
		else if(vet[f]>pivo)
			f--;
		else{
			int troca=vet[i];
			vet[i]=vet[f];
			vet[f]=troca;
			i++;
			f--;
		}
	}
	vet[beg]=vet[f];
	vet[f]=pivo;
	return f;
}

void quickSort(int *vet,int inicio,int fim)
{
	int posicaoPivo;			//pivo é o primeiro elementos
	if(vet!=NULL){
		if(inicio<fim){
			posicaoPivo=particiona(vet,inicio,fim);
			quickSort(vet,inicio,posicaoPivo-1);
			quickSort(vet,posicaoPivo+1,fim);
		}
	}
}


void test_case(int n,int q, int *ball,int *ques)
{

	quickSort(ball,0,n-1);
	for(int i=0;i<q;i++){
		int aux = binary_search(ball,ques[i],n);
		if(aux!= -1){
			printf("%d found at %d\n",ques[i],aux+1);
		}
		else
			printf("%d not found\n",ques[i]);
	}

}

int main()
{
	int N,Q;
	int balls[10000];
	int questions[10000];
	int cases = 1;

	while(1){

		scanf("%d %d",&N,&Q);
		if(N==0 && Q==0)
			break;

		for(int i=0;i<N;i++)
			scanf("%d",&balls[i]);

		for(int i=0;i<Q;i++)
			scanf("%d",&questions[i]);

		printf("CASE %d:\n",cases);
		test_case(N,Q,balls,questions);
		cases++;

	}

}
