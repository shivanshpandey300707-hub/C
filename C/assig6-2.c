 #include <stdio.h>

int main(void)
{
	int choice;
	double a, b;

	scanf("%d", &choice);
	scanf("%lf %lf", &a, &b);

	switch (choice) {
		case 1:
			printf("Addition: %.2f\n", a + b);
			break;
		case 2:
			printf("Subtraction: %.2f\n", a - b);
			break;
		case 3:
			printf("Multiplication: %.2f\n", a * b);
			break;
		case 4:
			if (b == 0) {
				printf("Error: Division by zero is not allowed.\n");
			} else {
				printf("Division: %.2f\n", a / b);
			}
			break;
		default:
			printf("Error: Invalid menu choice.\n");
	}

	return 0;
}
