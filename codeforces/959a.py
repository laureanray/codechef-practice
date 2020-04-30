# https://codeforces.com/problemset/problem/959/A

def solve(n):
    if n % 2 == 0:
        return 'Mahmoud'
    else: 
        return 'Ehab'

if __name__ == "__main__":
    n = int(input())

    print(solve(n))