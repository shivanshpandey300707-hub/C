#include <stdio.h>
#include <string.h>

int main(void) {
	const char pin1[] = "1234";
	const char pin2[] = "1234";

	if (strcmp(pin1, pin2) == 0) {
		printf("PIN matched.\n");
	} else {
		printf("Incorrect PIN.\n");
	}

	return 0;
}
