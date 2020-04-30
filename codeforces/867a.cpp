#include <bits/stdc++.h>
#define vi vector<int>
#define vs vector<string>
#define pb push_back
#define str string
#define in cin >> 
#define out cout <<
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

void println(vi a){
    for (int n : a) {
        cout << n << " ";
    }
    cout << endl;
}

void println(vs a){
    for (string n : a) {
        cout << n << " ";
    }
    cout << endl;
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, fs = 0, sf = 0;
    string s;
    in n;
    in s;
    
    if (n == 2 && s == "SF") {
        sf++;
    } else {
        for (int i = 0; i < (n - 1); i++) {
            if (s[i] == 'S' && s[i+1] == 'F') {
                sf++;
            } else if(s[i] == 'F' && s[i+1] == 'S') {
                fs++;
            }
        }
    }
  
    string res = (sf > fs) ? "YES" : "NO";
    println(res);
    return 0;    
}