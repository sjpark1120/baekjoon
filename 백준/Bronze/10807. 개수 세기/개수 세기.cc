#include<iostream>
using namespace std;

int main(void) {
    int n, x, v;
    int arr[201] = {};
    cin >> n;

    for (int i = 0; i < n; i++) { 
        cin >> x;
        arr[x + 100]++;
    }
    cin >> v;
    cout << arr[v+100];
    
}