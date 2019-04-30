#include <stdio.h>
#include <stdlib.h>



int *inicializa()
{
	int *output;

	output = (int*)malloc(sizeof(int)*21);

	for(int i=0;i<21;i++)
		output[i] = 0;

	return output;
}

int main()
{
	int N;
	int *countVector;
	int i;
	int num,max;	

	scanf("%d",&N);
	countVector=inicializa();

	for(i=0;i<N;i++){
		scanf("%d",&num);
		countVector[num-10]++;
	}
	max=countVector[1];

	for(i=0;i<21;i++){
		if(countVector[i]>max)
			max=countVector[i];
	}

	printf("%d\n",max);
	free(countVector);
}