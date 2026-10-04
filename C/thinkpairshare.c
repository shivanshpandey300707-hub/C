#include <stdio.h>

int main() {
    int arr[5] = {10, 20, 30, 40, 50};  

    
    printf("First element: %d\n", arr[0]);  
    printf("Last element: %d\n", arr[4]);   

    
    arr[2] = 99;

    
    for (int i = 0; i < 5; i++) {
        printf("arr[%d] = %d\n", i, arr[i]);
    }

    return 0;
}