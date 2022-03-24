#include <iostream>
using namespace std;

int AND(int a, int b)
{
	if (a == 0)
	{
		return 0;
	}
	else if (b == 0)
	{
		return 0;
	}
	else
	{
		return 1;
	}
}

int main()
{
	int a, b;
cout << "Digite o valor da porta A (1 ou 0): ";
cin >> a;
cout << "Digite o valor da porta B (1 ou 0): ";
cin >> b;

cout << "O valor da saida e: "<< AND(a,b);
}
