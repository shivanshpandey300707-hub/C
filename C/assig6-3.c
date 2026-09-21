 #include <stdio.h>

int main(void)
{
	int n;
	long long sum = 0;

	scanf("%d", &n);

	for (int i = 1; i <= n; ++i) {
		sum += i;
	}

	printf("Sum of the first %d natural numbers: %lld\n", n, sum);
	return 0;
}
