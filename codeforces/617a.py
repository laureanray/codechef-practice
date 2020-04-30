# https://codeforces.com/problemset/problem/617/A
x = int(input())
a = 0
if x > 5:
    a = x // 5
    x = x - (5 * a)
if x // 5 > 0:
    a = a + 1
    x = x - 5
if x // 4 > 0:
    a = a + 1
    x = x - 4
if x // 3 > 0:
    a = a + 1
    x = x - 3
if x // 2 > 0:
    a = a + 1
    x = x - 2
if x // 1 > 0:
    a = a + 1
    x = x - 1
print(a)
