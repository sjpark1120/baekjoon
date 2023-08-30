#include <stdio.h>

int main() {
    for (int i = 0; i < 3; i++) {
        int cnt = 0;
        int a[4];
        scanf("%d %d %d %d", &a[0], &a[1], &a[2], &a[3]);
        for (int j = 0; j < 4; j++) {
            if (a[j] == 0) {
                cnt++;
            }
        }
        if (cnt == 0) printf("E");
        else if (cnt == 1) printf("A");
        else if (cnt == 2) printf("B");
        else if (cnt == 3) printf("C");
        else printf("D");
        printf("\n");
    }
}
