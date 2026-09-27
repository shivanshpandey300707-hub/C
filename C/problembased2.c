#include <stdio.h>

int main(void) {
	int row, column;

	for (row = 1; row <= 3; row++) {
		for (column = 1; column <= row; column++) {
			printf("*");
			if (column < row) {
				printf(" ");
			}
		}
		printf("\n");
	}

	return 0;
}
