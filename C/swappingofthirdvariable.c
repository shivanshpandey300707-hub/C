#include<stdio.h>
int main(void)
{
        int first, second;

        printf("enter two integers: ");
        if (scanf("%d %d", &first, &second) != 2) {
            printf("invalid input.\n");
            return 1;
        }
    first = first + second;
    second = first - second;
    first = first - second;

    printf("after swapping: %d %d\n", first, second);
    return 0;


            
}