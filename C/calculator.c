#include <stdio.h>

int main(void)
{
	double num1, num2, result;
	char operator;
	char choice;

	do {
		printf("Enter an expression (e.g., 10 + 5): ");
		if (scanf("%lf %c %lf", &num1, &operator, &num2) != 3) {
			printf("Invalid input.\n");
			return 1;
		}

		switch (operator) {
		case '+':
			result = num1 + num2;
			break;
		case '-':
			result = num1 - num2;
			break;
		case '*':
			result = num1 * num2;
			break;
		case '/':
			if (num2 == 0) {
				printf("Error: division by zero.\n");
				break;
			}
			result = num1 / num2;
			break;
		default:
			printf("Invalid operator. Use +, -, *, or /.\n");
			break;
		}

		if ((operator == '+' || operator == '-' || operator == '*') ||
			(operator == '/' && num2 != 0)) {
			printf("Result: %.2f\n", result);
		}

		printf("Do you want to perform another operation? (y/n): ");
		if (scanf(" %c", &choice) != 1) {
			printf("Invalid input.\n");
			return 1;
		}
	} while (choice == 'y' || choice == 'Y');

	printf("Exiting calculator.\n");
	return 0;
}
