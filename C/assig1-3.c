 #include <stdio.h>

int main()
{
	long long a, b;

	if (scanf("%lld %lld", &a, &b) != 2)
		return 1;

	printf("Sum: %lld\n", a + b);
	printf("Difference: %lld\n", a - b);
	printf("Product: %lld\n", a * b);

	return 0;
}
