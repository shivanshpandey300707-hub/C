 #include <stdio.h>

int main(void)
{
	int number;

	do {
		printf("Enter a positive integer (negative number to stop): ");
		scanf("%d", &number);
	} while (number >= 0);

	return 0;
}
