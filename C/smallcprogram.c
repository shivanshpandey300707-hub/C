
#include <stdio.h>

int main(void)
{
	char character = 'A';
	int integer = 42;
	float floating_point = 3.14f;
	double double_precision = 2.718281828;

	printf("char: %c\n", character);
	printf("int: %d\n", integer);
	printf("float: %f\n", (double)floating_point);
	printf("double: %f\n", double_precision);

	return 0;
}
