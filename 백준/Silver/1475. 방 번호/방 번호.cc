#include<iostream>
#include <string>
using namespace std;

int main(void) {
    string n;
    int arr[9] = {};
    int max = 0;
    cin >> n;
    for (int i = 0; i < n.length(); i++) {
        if (n[i] - '0' == 9) arr[6]++;
         else arr[n[i]-'0']++;
    }
    if (arr[6] % 2 != 0) arr[6] = arr[6] / 2 + 1;
    else arr[6] = arr[6] / 2;

    for (int i = 0; i < 9; i++) {
        if (max < arr[i]) max = arr[i];
    }
    cout << max;
}