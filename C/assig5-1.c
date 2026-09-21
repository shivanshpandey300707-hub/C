 #include <stdio.h>

int main(void)
{
	double a, b, result;
	char operator;

	scanf("%lf %lf %c", &a, &b, &operator);

	switch (operator) {
	case '+':
		result = a + b;
		printf("Result: %g\n", result);
		break;
	case '-':
		result = a - b;
		printf("Result: %g\n", result);
		break;
	case '*':
		result = a * b;
		printf("Result: %g\n", result);
		break;
	case '/':
		if (b == 0) {
			printf("Division by zero is not allowed\n");
		} else {
			result = a / b;
			printf("Result: %g\n", result);
		}
		break;
	default:
		printf("Invalid operator\n");
	}

	return 0;
}
