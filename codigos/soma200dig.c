#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int getMax(int a,int b)
{
	if(a>=b) return a;
	else return b;
}


/*
void soma(char str1[],char str2[],char *str3[])
{
	int i,len1,len2,dig1,dig2,dig3,aux;
	char str3[202];
	int vaiUm,max;

	for(i=0;i<201;i++)
		str3[i] = '0';

	str3[201]='\0';

	len1 = strlen(str1);
	len2 = strlen(str2);
	max = getMax(len1,len2);
	len1--;
	len2--;
	max-=2;

	while(1){
		
		if(str1[len1] == '0'){
			
			dig1 = str2[len2] - '0';
			dig2 = str3[max] - '0';

			aux = dig1 +dig2;
			str3[max] = (aux%10) + '0';
			if(aux/10>0){
				str3[max-1] = (aux/10) + '0';
			}
			max--;
			break;

		}

		if(str2[len2] == '0'){
			
			dig1 = str1[len1] - '0';
			dig2 = str3[max] - '0';

			aux = dig1 +dig2;
			str3[max] = (aux%10) +'0';
			if(aux/10>0){
				str3[max-1] = (aux/10) + '0';
			}
			max--;
			break;

		}

		dig1 = str1[len1] - '0';
		dig2 = str2[len2] - '0';
		dig3 = str3[max] - '0';

		aux = dig1 + dig2 + dig3 ;
		vaiUm = aux/10;

		str3[max] = (aux%10) + '0';
		str3[max-1] = (vaiUm) + '0';

		len1--;
		len2--;
		max--;
	}




}
*/

int main()
{

	char str1[202],str2[202];
	char str3[202];
	int i,len1,len2,dig1,dig2,dig3,aux;
	int vaiUm,max;
	

	fgets(str1,201,stdin);
	fgets(str2,201,stdin);
	

	for(i=0;i<201;i++)
		str3[i] = '0';

	str3[201]='\0';

	len1 = strlen(str1);
	len2 = strlen(str2);
	max = getMax(len1,len2);
	len1--;
	len2--;
	max-=2;

	while(1){
		
		if(str1[len1] == '0'){
			
			dig1 = str2[len2] - '0';
			dig2 = str3[max] - '0';

			aux = dig1 +dig2;
			str3[max] = (aux%10) + '0';
			if(aux/10>0){
				str3[max-1] = (aux/10) + '0';
			}
			max--;
			break;

		}

		if(str2[len2] == '0'){
			
			dig1 = str1[len1] - '0';
			dig2 = str3[max] - '0';

			aux = dig1 +dig2;
			str3[max] = (aux%10) +'0';
			if(aux/10>0){
				str3[max-1] = (aux/10) + '0';
			}
			max--;
			break;

		}

		dig1 = str1[len1] - '0';
		dig2 = str2[len2] - '0';
		dig3 = str3[max] - '0';

		aux = dig1 + dig2 + dig3 ;
		vaiUm = aux/10;

		str3[max] = (aux%10) + '0';
		str3[max-1] = (vaiUm) + '0';

		len1--;
		len2--;
		max--;
	}	


	puts(str3);

}