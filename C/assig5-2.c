 #include <stdio.h>

int main(void)
{
	int choice;
	double a, b;

	if (scanf("%d", &choice) != 1) {
		printf("Invalid menu choice.\n");
		return 1;
	}

	if (scanf("%lf %lf", &a, &b) != 2) {
		printf("Invalid input.\n");
		return 1;
	}

	switch (choice) {
		case 1:
			printf("Addition result: %.2f\n", a + b);
			break;
		case 2:
			printf("Subtraction result: %.2f\n", a - b);
			break;
		case 3:
			printf("Multiplication result: %.2f\n", a * b);
			break;
		case 4:
			if (b == 0.0) {
				printf("Error: Division by zero is not allowed.\n");
			} else {
				printf("Division result: %.2f\n", a / b);
			}
			break;
		default:
			printf("Invalid menu choice.\n");
	}

	return 0;
}
