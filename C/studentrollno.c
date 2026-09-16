#include <stdio.h>

int main(void)
{
	int roll_number;
	float mark1, mark2, mark3;
	float total, average;

	printf("Enter roll number: ");
	scanf("%d", &roll_number);

	printf("Enter marks for three subjects: ");
	scanf("%f %f %f", &mark1, &mark2, &mark3);

	total = mark1 + mark2 + mark3;
	average = total / 3.0f;

	printf("\nRoll number: %d\n", roll_number);
	printf("Total marks: %.2f\n", total);
	printf("Average marks: %.2f\n", average);

	return 0;
}
