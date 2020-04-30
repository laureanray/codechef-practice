# https://codeforces.com/problemset/problem/1186/A
def solve(n, m, k):
    if m >= n and k >= n:
        return 'Yes'
    return 'No'

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    print(solve(n, m, k))