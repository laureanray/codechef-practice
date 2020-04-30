# https://codeforces.com/problemset/problem/263/A
if __name__ == "__main__":
    matrix = []
    r = 0
    col = 0
    ans = 0
    for i in range(5):
        row = list(map(int, input().split()))
        if 1 in row:
            ans = abs(i - 2) + abs(row.index(1) - 2)

    print(ans)