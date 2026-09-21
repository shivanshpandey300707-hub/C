/* Example: I brush my teeth every morning and evening.
 * This repeats every day, just like a loop repeats instructions.
 * Pair up and share: each pair of teeth-brushing times is printed.
 */
#include <stdio.h>

int main(void)
{
	const char *times[] = {"morning", "evening"};

	for (int i = 0; i < 2; i++) {
		printf("I brush my teeth in the %s.\n", times[i]);
	}

	return 0;
}
