#include <bits/stdc++.h>
#define vi vector<int>

using namespace std;

const int MAX = 1e5+5;

void println(char c) {
    cout << c << endl;
}

void println(string s) {
    cout << s << endl;
}

void println(int n ){
    cout << n << endl;
}


void println(vector<int> a){
    for (int n : a) {
        cout << n << " ";
    }
    cout << endl;
}

void solve(int n) {
    if (n == 2) {
        cout << 2 << endl;
    } else if (n % 2 != 0) {
        cout << 1 << endl;
    } else {
        cout << 0 << endl;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int q, n;
    cin >> q;

    for (int i = 0; i < q; i++) {
        cin >> n;
        solve(n);
    }
    return 0;    
}