#include <stdio.h>

int main(void)
{
    int num1, num2, result;

    printf("Enter two integers: ");
    scanf("%d %d", &num1, &num2);

    result = num1 - num2;

    printf("Subtraction: %d\n", result);

    return 0;
}