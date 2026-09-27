#include <stdio.h>

int main() {

	int i, j;
	int num = 1; // Starting number

	// Outer loop for rows
	for (i = 1; i <= 3; i++) {
		// Inner loop for columns
		for (j = 1; j <= 3; j++) {
			printf("%d ", num);
			num++; // Increment number
		}
		printf("\n"); // Move to the next row
	}

return 0;
}