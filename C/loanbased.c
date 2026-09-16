#include <stdio.h>

int main() {
    int age;
    double salary;

    printf("Enter age: ");
    scanf("%d", &age);

    printf("Enter salary: ");
    scanf("%lf", &salary);

    if (age >= 21 && salary >= 25000) {
        printf("Eligible for a loan.\n");
    } else {
        printf("Not eligible for a loan.\n");
    }

    return 0;
}