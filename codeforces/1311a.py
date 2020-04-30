# https://codeforces.com/problemset/problem/1311/A

# even a = a - y
# odd a = a + y
# 7 4
def solve(a, b):
    moves = 0
    get = 0
    if a == b:
        return 0
    elif a < b:
        get = b - a
        moves = moves + 1
        if get % 2 == 0:
            moves = moves  + 1
    elif a > b:
        get = a - b
        moves = moves + 1
        if get % 2 != 0:
            moves = moves + 1
    return moves


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        a, b = map(int, input().split())
        print(solve(a, b))
