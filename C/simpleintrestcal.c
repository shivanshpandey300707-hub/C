#include <stdio.h>

int main(void)
{
	double principal, rate, time, simple_interest;

	printf("Enter principal amount: ");
	scanf("%lf", &principal);

	printf("Enter annual interest rate (%%): ");
	scanf("%lf", &rate);

	printf("Enter time in years: ");
	scanf("%lf", &time);

	simple_interest = (principal * rate * time) / 100.0;

	printf("Simple interest: %.2f\n", simple_interest);
	printf("Total amount: %.2f\n", principal + simple_interest);

	return 0;
}