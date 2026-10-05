#include <stdio.h>

int main(void)
{
	const char *times[] = {"morning", "evening"};

	for (int i = 0; i < 2; i++) {
		printf("I brush my teeth in the %s.\n", times[i]);
	}

	return 0;
}
