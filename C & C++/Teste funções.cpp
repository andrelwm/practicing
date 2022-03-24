#include<iostream>
using namespace std;

int descobreIdade(int anoAtual, int anoNas);

int main()
{
	cout<<descobreIdade(2021, 1993);
	system("pause");
	return 0;
}

int descobreIdade(int anoAtual, int anoNas)
{

  return anoAtual - anoNas;

}
