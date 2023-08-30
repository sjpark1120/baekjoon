#include <stdio.h>
#include<algorithm>
using namespace std;

int main() {
    int a[3];
    scanf("%d %d %d", &a[0], &a[1], &a[2]);
    sort(a, a+3);
    for (int i = 0; i < 3; i++) {
        printf("%d ", a[i]);
    }
}