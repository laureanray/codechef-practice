#include <bits/stdc++.h>
#define vi vector<int>

using namespace std;

const int MAX = 1e5+5;

void print(char c) {
    cout << c << endl;
}

void print(string s) {
    cout << s << endl;
}

void print(int n ){
    cout << n << endl;
}

void solve(string s, int num) {
    int one = 0, zero = 0;

    for (char c: s) {
        switch(c) {
            case 'z':
                zero++;
                break;
            case 'n':
                one++;
                break;
        }
    }

    if (one > 0) {
        for(int i = 0; i < one; i++){
            cout << '1' << " ";
        }
    }
    
    if (zero > 0) {
        for (int i = 0; i < zero; i++) {
            cout << '0' << " ";
        }
    }

}

void print_vector(vi v) {
    for (int n : v) {
        cout << n << " ";
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    string s;

    cin >> n;
    cin >> s;

    solve(s, n); 
    return 0;    
}