 #include <stdio.h>

int main(void)
{
	float marks;

	printf("Enter the student's marks: ");
	scanf("%f", &marks);

	if (marks > 50)
		printf("Pass\n");
	else
		printf("Fail\n");

	return 0;
}
