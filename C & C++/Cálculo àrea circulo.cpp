#include <stdio.h>
//#define PI 3.1415

int main(void) {
	
	float raio, area;
	const float pi = 3.1415;
	
	printf("Digite o raio da circunferencia (em metros): ");
	scanf("%f", &raio);
	
	pi = 5;
	
	area = pi * (raio*raio);
	
	printf("\nA area da circunferencia de raio %.2f e: %.2f\n", raio, area);
	
	return 0;
	
}
