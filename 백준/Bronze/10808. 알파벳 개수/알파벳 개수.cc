#include<iostream>
using namespace std;

int main(void) {
    string s;
    int arr[26] = { 0, };
    cin >> s;

    for (int i = 0; i < s.length(); i++) { //a = 97
        arr[(int)s[i] - 97]++;
    }

    for (int i = 0; i < 26; i++) { //a = 97
        cout << arr[i] << ' ';
    }
}