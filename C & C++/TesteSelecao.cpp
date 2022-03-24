#include <iostream>
using namespace std;

void selecao(int vet[], int tam);
int main(int argc, char** argv) {
	
	int x, vetor[] = {13, 45, 10, 50, 3};
	
	for (x = 0; x < 5; x++){
		cout << vetor[x] << "\t";
	}
	
	selecao(vetor, 5);
	
	cout << "\n\n";
	
	for (x = 0; x < 5; x++){
		cout << vetor[x] << "\t";
	}
	
	system("pause");
}

void selecao(int vet[], int tam){
	
	int j, i, aux, temp;
	for (i = 0; i < tam -1; i++){
		aux = i;
		for (j = i + 1; j < tam; j++){
			if(vet[aux] > vet[j]){
				aux = j;
			}
		temp = vet[aux];
		vet[aux] = vet[i];
		vet[i] = temp;
		}
	}
}
