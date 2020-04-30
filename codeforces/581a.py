# https://codeforces.com/problemset/problem/581/A

if __name__ == "__main__":
    a, b = map(int, input().split())
    total = a + b
    largest = a if a > b else b
    hip = 0
    remain = 0

    while a > 0 and b > 0:
        a = a - 1
        b = b - 1
        hip = hip + 1

    remain = (a // 2) if a > 0 else (b // 2)

    print(hip, remain, sep=' ')