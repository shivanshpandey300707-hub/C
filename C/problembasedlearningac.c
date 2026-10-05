#include <stdio.h>

#define STUDENT_COUNT 5

int main(void)
{
	float marks[STUDENT_COUNT];
	float total = 0.0f;

	for (int i = 0; i < STUDENT_COUNT; ++i) {
		printf("Enter marks for student %d: ", i + 1);
		if (scanf("%f", &marks[i]) != 1) {
			printf("Invalid input.\n");
			return 1;
		}
		total += marks[i];
	}

	printf("Average marks: %.2f\n", total / STUDENT_COUNT);

	/* To handle 100 students, change STUDENT_COUNT to 100. The array,
	   input loop, and average calculation all adjust automatically. */
	return 0;
}
