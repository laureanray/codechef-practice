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

void print(vi a){
    for (int n : a) {
        cout << n << " ";
    }
}

void print(float a) {
    cout << a;
}

float ave(vi nums) {
    int sum = 0;
    for (int num : nums) {
        sum += num;
    }

    return sum / nums.size();
}

void solve(int t, int n, int m, vi scores){
    // cout << "TEST CASE #" << t << endl;
    int usable_scores = 0;
    for(int i = 1; i < n; i++) {
        usable_scores += scores[i];
    }

    while(scores[0] < m && usable_scores > 0) {
        scores[0]++;
        usable_scores--;
    }

    println(scores[0]);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int test_case, n, m;
    in test_case;

    for (int i = 0; i < test_case; i++) {
        cin >> n >> m;
        vi scores;
        for (int j = 0; j < n; j++) {
            int temp;
            cin >> temp;
            scores.push_back(temp);
        }
        solve(i, n, m, scores);
    }


   
    return 0;    
}