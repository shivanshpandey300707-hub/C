#include <stdio.h>

int main(void)
{
	int a, b;

	scanf("%d %d", &a, &b);

	printf("Logical AND (a && b): %d\n", a && b);
	printf("Logical OR (a || b): %d\n", a || b);
	printf("Logical NOT (!a): %d\n", !a);
	printf("Bitwise AND (a & b): %d\n", a & b);
	printf("Bitwise OR (a | b): %d\n", a | b);
	printf("Bitwise XOR (a ^ b): %d\n", a ^ b);
	printf("Left shift (a << b): %d\n", a << b);
	printf("Right shift (a >> b): %d\n", a >> b);

	return 0;
}
