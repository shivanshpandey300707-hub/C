#include <stdio.h>
int external_value = 100;
void show_storage_classes(void)
{
	auto int automatic_value = 10;
	register int register_value = 20;
	static int static_value = 0;
	extern int external_value;
	++static_value;
	printf("  auto:     %d (local to this call)\n", automatic_value);
	printf("  register: %d (local variable; address cannot be taken)\n", register_value);
	printf("  static:   %d (retains value between calls)\n", static_value);
	printf("  extern:   %d (defined outside this function)\n", external_value);
}
int main(void)
{
	puts("First call:");
	show_storage_classes();
	puts("\nSecond call:");
	show_storage_classes();
	return 0;
}




