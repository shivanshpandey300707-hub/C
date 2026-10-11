#include <stdio.h>

int main(void)
{
	const char *students[6] = {
		"shivansh",
		"dewansh",
		"vaibhav",
		"lakshay",
		"rehan",
		"divyansh"
	};

	for (int i = 0; i < 6; i++) {
		printf("%s\n", students[i]);
	}

	return 0;
}
