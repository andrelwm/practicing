#include <iostream>
using namespace std;

void selecao(int vet[], int tam)
{
	int j, i, aux, temp;
	for(i = 0; i < (tam - 1); i++)
	{
		aux = i;
		for(j = i; j < tam; j++)
		{
			if(vet[aux] > vet[j])
			{
				aux = j;
			}
			temp = vet[aux];
			vet[aux] = vet[i];
			vet[i] = temp;
		}
	}
}

int main()
{
	int x, vet[] = {3, 35, 2, 100, 54, 72, 64};
	selecao(vet, 7);
	for (x = 0; x < 7; x++)
	{
		cout << vet[x] << "\t";
	}
	system("pause");
}



