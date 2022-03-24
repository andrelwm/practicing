#include <stdio.h>

int main() {
	
	float numero1, numero2, numero3, media;
	
	printf("Digite 3 numeros (apertando enter apos digitar cada um): \n");
	scanf("%f", &numero1);
	scanf("%f", &numero2);
	scanf("%f", &numero3);
	
	media = (numero1 + numero2 + numero3)/3;
	
	printf("%.2f, %.2f, %.2f e media: %.2f", numero1, numero2, numero3, media);
	
	return 0;
}
