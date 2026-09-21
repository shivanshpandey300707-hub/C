/* Demonstrate basic C data types, constants, and arithmetic. */
#include <stdio.h>

#define CONSTANT_VALUE 100

int main(void)
{
	int a, b, sum;
	float sampleFloat = 3.14f;
	double sampleDouble = 2.718281828;
	char sampleChar = 'C';

	if (scanf("%d %d", &a, &b) != 2) {
		return 1;
	}

	sum = a + b;

	printf("a = %d\n", a);
	printf("b = %d\n", b);
	printf("Sum = %d\n", sum);
	printf("Constant value = %d\n", CONSTANT_VALUE);
	printf("Float value = %.2f\n", sampleFloat);
	printf("Double value = %.9f\n", sampleDouble);
	printf("Char value = %c\n", sampleChar);

	return 0;
}
