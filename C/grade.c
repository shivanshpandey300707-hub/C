 #include <stdio.h>

int main(void)
{
	int marks;

	printf("Enter marks (0-100): ");
	if (scanf("%d", &marks) != 1 || marks < 0 || marks > 100) {
		printf("Invalid marks.\n");
		return 1;
	}

	if (marks >= 90)
		printf("Grade: A\n");
	else if (marks >= 80)
		printf("Grade: B\n");
	else if (marks >= 70)
		printf("Grade: C\n");
	else if (marks >= 60)
		printf("Grade: D\n");
	else
		printf("Status: Fail\n");

	return 0;
}
