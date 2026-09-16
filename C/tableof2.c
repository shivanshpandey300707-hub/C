#include <stdio.h>

int main(void)
{
	printf("Multiplication Table of 2\n");
	printf("=========================\n");

	for (int i = 1; i <= 10; i++) {
		printf("2 x %2d = %2d\n", i, 2 * i);
	}

	return 0;
}