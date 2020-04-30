# https://codeforces.com/problemset/problem/1283/A

def solve(h, m):
    minutes = (23 - h) * 60
    return minutes + (60 - m)

if __name__ == "__main__":
    T = int(input())

    for i in range(T):
        h, m = map(int, input().split())
        print(solve(h, m)) 