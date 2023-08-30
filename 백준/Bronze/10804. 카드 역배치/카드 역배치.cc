#include <stdio.h>
int main() {
    int arr[20] = { 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 };
    int a, b;
    for (int i = 0; i < 10; i++) {
        scanf("%d %d", &a, &b);
        int x = b - a+1;
        for (int j = 0; j < x/2; j++) {
            int tmp = arr[a+j-1];
            arr[a+j-1] = arr[b-j-1];
            arr[b-j-1] = tmp;
        }
    }
    for (int i = 0; i < 20; i++) {
        printf("%d ", arr[i]);
    }
}