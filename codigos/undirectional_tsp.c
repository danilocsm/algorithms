
//Unidirectional TSP

#include <stdio.h>

 

int n, m;

int M[10][100];

int ant[10][100];

 

int path(int lin, int col) {

 

	if(col==0) return M[lin][col];

	 

	int cima, lado, baixo, MIN, aux;

	 

	lado = path(lin,col-1) + M[lin][col];

	cima = path(lin==0 ? n-1 : lin-1, col-1) + M[lin][col];

	baixo = path(lin==n-1 ? 0 : lin+1, col-1) + M[lin][col];

	 

	MIN = lado;

	ant[lin][col] = lin;

	if(cima<MIN) {

		MIN = cima; 

		ant[lin][col] = lin==0 ? n-1 : lin-1;

	}

	if(cima==MIN) {

		if(lin==0 ? n-1 : lin-1 < ant[lin][col]) {

			ant[lin][col] = lin==0 ? n-1 : lin-1;

		}

	}

	 

	if(baixo<MIN) {

	    MIN = baixo;

	    ant[lin][col] = lin==n-1 ? 0 : lin+1;

	}

	if(baixo==MIN) {

		if( lin==n-1 ? 0 : lin+1 < ant[lin][col] ) {

			ant[lin][col] = lin==n-1 ? 0 : lin+1;

		}

	}

	 

	return MIN;

}

 

void printPath(int lin, int col) {

	if(col==0) {

		printf("%d", lin+1);

	}

	else {

		printPath( ant[lin][col], col-1 );

		printf(" %d", lin+1);

	}

}

 

int main() {

	while(scanf("%d%d", &n, &m)!=EOF) {

		for(int i=0; i<n; i++) {

			for(int j=0; j<m; j++) {

				scanf("%d", &M[i][j]);

		//printf("%d ", M[i][j]);

			}

	//printf("\n");

		}


		int MIN, AUX, minPath;

		MIN = path(0, m-1);

		minPath = 0;

		for(int i=1; i<n; i++) {

			AUX = path(i, m-1);

			if(AUX<MIN) {

				MIN = AUX;

				minPath = i;

			}

		}

		 

		printPath(minPath, m-1);

		printf("\n%d\n", MIN);

	}

}

