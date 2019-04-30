#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *  itoa ( int value, char * str )
{
    char temp;
    int i =0;
    while (value > 0) {
        int digito = value % 10;

        str[i] = digito + '0';
        value /= 10;
        i++;

    }
   i = 0;
   int j = strlen(str) - 1;

   while (i < j) {
      temp = str[i];
      str[i] = str[j];
      str[j] = temp;
      i++;
      j--;
   }
    return str;


}


void show_playlist(int *vet,int size,int soma)
{
    char buffer[20000];

    for(int i=0;i<size;i++){
        printf("%d ",vet[i]);
    }
    itoa(soma,buffer);
    printf("sum:%s\n",buffer);
}

void constroy_playlist(int n,int num,int *faixas)
{
    int max = 20;
    int aux[num];
    int sum = 0;
    for(int i=0;i<num;i++){
            sum += faixas[i];
            if(sum<=n){
                aux[i] = faixas[i];
            }
            else{

            }
    }

}

int main()
{
    int N,num_faix;
    int *faixas;
    int sum = 0;
    while(1){

        scanf("%d %d",&N,&num_faix);
        if(N==0)
            exit(1);

        faixas = (int*)malloc(sizeof(int)*num_faix);
        for(int i=0;i<num_faix;i++){
            scanf("%d",&faixas[i]);
            sum += faixas[i];
        }
        if(sum<=N){
            show_playlist(faixas,num_faix,sum);
        }
        else
            constroy_playlist(N,num_faix,faixas);
    }

}
