#include <bits/stdc++.h>
#define vi vector<int>
#define vs vector<string>
#define pb push_back
#define str string
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

void solve(int n, int m, vs s, vs t, int q, vi years) {
    for (int i = 0; i < q; i++) {
        int year = years.at(i) - 1;
        println(s.at(year % s.size()) + t.at(year % t.size()););
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<string> s;
    vector<string> t;
    vector<int> years;

    int n, m, q;    

    cin >> n >> m;
    
    for (int i = 0; i < n; i++) {
        string a;
        cin >> a;
        s.pb(a);
    }

    for (int i = 0; i < m; i++) {
        string a;
        cin >> a;
        t.pb(a);
    }

    cin >> q;

    for (int i = 0; i < q; i++) {
        int year;
        cin >> year;
        years.pb(year);
    }

    solve(m, n, s, t, q, years);

    return 0;    
}