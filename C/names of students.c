#include <stdio.h>
#include <string.h>

int main(void)
{
	char students[9][6][100];

	for (int table = 0; table < 9; table++) {
		for (int seat = 0; seat < 6; seat++) {
			printf("Enter the name of the student at table %d, seat %d: ",
				   table + 1, seat + 1);
			if (fgets(students[table][seat], sizeof students[table][seat], stdin) == NULL) {
				return 1;
			}
			students[table][seat][strcspn(students[table][seat], "\n")] = '\0';
		}
	}

	printf("\nStudents in the classroom:\n");
	for (int table = 0; table < 9; table++) {
		printf("Table %d:\n", table + 1);
		for (int seat = 0; seat < 6; seat++) {
			printf("  %s\n", students[table][seat]);
		}
	}

	return 0;
}
