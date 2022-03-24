#include<iostream>
using namespace std;

double media(double [], int tam);

int main()
{
	double notas[5];
	for (int x=0; x<5; x++)
	{
		cout<<"\nNota "<<x+1<<": ";
		cin>>notas[x];
	}
	cout<<"\n\nRelacao das notas originais\n";
	for (int x=0; x<5; x++)
	cout<<notas[x]<<"\t";
	cout<<"\n\nMedia da turma: "<<media(notas, 5);
	cout<<"\n\n";
	system("pause");
	return 0;
}

double media(double n[], int tam)
{
	double soma=0;
	for (int x = 0; x < tam; x++)
	soma += n[x];
	return soma/tam;
}
