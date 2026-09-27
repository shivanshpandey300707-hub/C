#include <stdio.h>

int main() {
	int i, j;
	int rows = 3; // Number of rows

	// Print a decreasing triangle of stars.
	for (i = rows; i >= 1; i--) {
		for (j = 1; j <= i; j++) {
			printf("*");
		}
		printf("\n");
	}

	return 0;
}