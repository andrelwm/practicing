#include <iostream>
#include <cctype>
using namespace std;
int main()
{
	struct cad
	{
		char pal[21];
	}palavra[2];
	int x, y;
	for (x = 0; x < 2; x++)
	{
		cout << "\nPalavra: ";
		cin.getline(palavra[x].pal, 21);
	}
	palavra[0].pal[0] = toupper(palavra[0].pal[0]);
	system("cls");
	for (x = 0; x < 2; x++)
	{
		for(y = 0; palavra[x].pal[y] != '\0'; y++)
		{
			cout << ' ' << palavra[x].pal[y];
		}
		cout << "\n\n";
	}
	cout << "\n\n";
	system("pause");
}
