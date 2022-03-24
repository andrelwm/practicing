#include <iostream>
using namespace std;

int main()
{
	struct coordenadas
	{
		int x, y;
	};
	
	coordenadas a, b;
	cout << "\nDigite as coordenadas de A:\n";
	cin >> a.x;
	cin.get();
	cin >> a.y;
	cin.get();
	cout << "\nDigite as coordenadas de B:\n";
	cin >> b.x;
	cin.get();
	cin >> b.y;
	cin.get();
	
	cout << "\nCoordenadas de A: (" << a.x << ", " << a.y << ")";
	cout << "\nCoordenadas de B: (" << b.x << ", " << b.y << ")";
	cout << "\n\n";
	system("pause");
}
