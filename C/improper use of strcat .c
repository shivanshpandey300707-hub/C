#include <stdio.h>
#include <string.h>

int main(void)
{
	char first[50] = "John"; 
	char last[] = "Doe";

	strcat(first, " ");
	strcat(first, last);
	printf("Full Name: %s\n", first);

	return 0;
}
