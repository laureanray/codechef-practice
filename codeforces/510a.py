# https://codeforces.com/problemset/problem/510/A

def draw(n, m):
    toggle = True
    for i in range(n):
        if i % 2 != 0: 
            # odd
            toggle = not toggle
        for j in range(m):
            if i % 2 != 0 and toggle:
                if j != m - 1:
                    print('.', end='')
                else:
                    print('#', end='')
            elif i % 2 != 0 and not toggle:
                if j != 0:
                    print('.', end='')
                else:
                    print('#', end='')
            else:
                print('#', end='')
        print()

if __name__ == "__main__":
    n, m = map(int, input().split())

    draw(n, m)