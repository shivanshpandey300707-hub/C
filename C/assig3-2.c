/* Demonstration of the dangling else problem. */
#include <stdio.h>

int main(void)
{
	int x, y, choice;
	const char *unbraced = "no statement executed";
	const char *braced = "no statement executed";

	if (scanf("%d %d %d", &x, &y, &choice) != 3 ||
		(choice != 0 && choice != 1)) {
		return 1;
	}

	/* Without braces, the else is associated with the nearest if. */
	if (choice)
		if (x > y)
			unbraced = "x is greater than y";
		else
			unbraced = "x is not greater than y";

	/* With braces, the else is explicitly associated with the outer if. */
	if (choice) {
		if (x > y)
			braced = "x is greater than y";
	} else {
		braced = "outer condition is false";
	}

	printf("Unbraced version: %s\n", unbraced);
	printf("Braced version:   %s\n", braced);

	return 0;
}
