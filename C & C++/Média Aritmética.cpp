#include <stdio.h>

int main() {
	
	float numero1, numero2, numero3, media;
	
	numero1 = 10;
	numero2 = 15;
	numero3 = 75;
	
	media = (numero1 + numero2 + numero3)/3;
	
	printf("A media dos numeros %.2f, %.2f e %.2f eh: %.2f", numero1, numero2, numero3, media);
	
	return 0;
}
