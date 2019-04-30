#include <stdio.h>
#include <math.h>



int countMultiples(int a,int b, int c)
{	
	int count = 0;
	int aux;
	
    if (a%c == 0 || b%c == 0)
        count +=1;
	
    aux = (b-a);

    if (aux+c>b){
	
        count += ((b-a)/c);
        return count;
	}
	aux = (double)((b-a)/c);
    count +=ceil(aux);
    
    return count;
}

int main()
{
	int a,b,c;
	int count;
	
	scanf("%d",&a);
	scanf("%d",&b);
	scanf("%d",&c);
	
	count = countMultiples(a,b,c);
	
	printf("%d\n",count);
	
	
}
