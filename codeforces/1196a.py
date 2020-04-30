# https://codeforces.com/problemset/problem/1196/A

def solve(a, b, c):
    return (a + b + c) // 2

if __name__ == "__main__":
    T = int(input())

    for i in range(T):
        a, b, c = map(int, input().split())
        print(solve(a, b, c))

    