#include <stdio.h>
#include <algorithm>
using namespace std;
int main() {
    int a[5];
    int sum = 0;
    for (int i = 0; i < 5; i++) {
        scanf("%d", &a[i]);
        sum += a[i];
    }
    sort(a, a + 5);
    printf("%d\n", sum / 5);
    printf("%d", a[2]);
}
