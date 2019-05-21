#include <stdio.h>
#include <string.h>
#define SIZANSWER 1000

char resposta[SIZANSWER];
int resto = 0;
int tracker = SIZANSWER - 2;

void sum(char a, char b){
	int a_v = a - '0';
	int b_b = b - '0';

	int sum = a_v + b_b + resto;

	int new_v = sum % 10;

	if(sum >= 10) resto = 1;
	else resto = 0;

	//printf("%c<<\n", new_v + '0');
	resposta[tracker] = new_v + '0';

	tracker--;
}

void do_sum(char v1[], char v2[]){
	int size_a = strlen(v1) - 1;
	int size_b = strlen(v2) - 1;

	int bigger = size_a > size_b ? size_a : size_b;
	bigger++;

	while(bigger--){
		if(size_b < 0){
			sum(v1[size_a], '0');
		} else if(size_a < 0){
			sum('0', v2[size_b]);
		} else {
			sum(v1[size_a],  v2[size_b]);
		}

		size_a--;
		size_b--;
	}

	resposta[tracker] = resto + '0';
}

int main(){
	int i;

	for(i = 0; i < SIZANSWER; i++) resposta[i] = '0';
	resposta[SIZANSWER-1] = '\0';

	char a[202], b[202];

	scanf("%s %s", a, b);

	if(!strcmp(a, "0") && !strcmp(b, "0")){
		printf("0\n");
		return 0;
	}

	do_sum(a, b);

	i = 0;
	while(resposta[i] == '0'){
		i++;
	}

	printf("%s\n", resposta + i);

}
