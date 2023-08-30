#include<iostream>
#include <string>
using namespace std;
int arr[20000005] = {};
int in_arr[1000005] = {};
int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, x, tmp;
    int sum = 0;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> tmp;
        in_arr[i] = tmp;
        arr[tmp] = 1;
    }
    cin >> x;

    for (int i = 0; i < n; i++) {
        if (x - in_arr[i] > 0 && arr[x - in_arr[i]] == 1) sum++;
    }
    cout << sum/2;
}