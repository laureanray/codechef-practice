# https://codeforces.com/problemset/problem/791/A
if __name__ == "__main__":
    a, b = map(int, input().split())
    year = 0
    while True:
        year = year + 1
        a = a * 3
        b = b * 2
        if a > b:
            break
    print(year)