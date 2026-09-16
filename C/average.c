#include <stdio.h>

int main() {
    int num1, num2, num3, average;

    printf("enter three numbers: ");
    scanf("%d %d %d", &num1, &num2, &num3);

        average = (num1 + num2 + num3) / 3.0;

        printf("average = %d\n", average);
        return 0;
}