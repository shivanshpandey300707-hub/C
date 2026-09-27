#include <stdio.h>

int main(void) {
    for (int i = 1; i <= 3; i++) {
        for (int j = 1; j <= i; j++) {
            printf("%d", i);
            if (j < i) {
                printf(" ");
            }
        }
        printf("\n");
    }

    return 0;
}