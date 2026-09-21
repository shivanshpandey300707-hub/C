 #include <stdio.h>

int main(void)
{
	int a, b;

	scanf("%d %d", &a, &b);

	printf("Sum: %d\n", a + b);
	printf("Difference: %d\n", a - b);
	printf("Product: %d\n", a * b);
	printf("Quotient: %d\n", a / b);

	if (a > b)
		printf("Comparison: First number is greater than the second number.\n");
	else if (a < b)
		printf("Comparison: First number is less than the second number.\n");
	else
		printf("Comparison: First number is equal to the second number.\n");

	return 0;
}
