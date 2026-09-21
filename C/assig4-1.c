 #include <stdio.h>

int main(void)
{
	double a, b, result;
	char operator;

	if (scanf("%lf %lf %c", &a, &b, &operator) != 3) {
		return 1;
	}

	switch (operator) {
		case '+':
			result = a + b;
			printf("Result: %.2f\n", result);
			break;
		case '-':
			result = a - b;
			printf("Result: %.2f\n", result);
			break;
		case '*':
			result = a * b;
			printf("Result: %.2f\n", result);
			break;
		case '/':
			if (b == 0) {
				printf("Division by zero is not allowed\n");
			} else {
				result = a / b;
				printf("Result: %.2f\n", result);
			}
			break;
		default:
			printf("Invalid operator\n");
	}

	return 0;
}
