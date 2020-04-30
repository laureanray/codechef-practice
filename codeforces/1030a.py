# https://codeforces.com/problemset/problem/1030/A

if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    is_hard = False
    for num in numbers:
        if num == 1:
            is_hard = True
            break
    
    print('HARD' if is_hard else 'EASY')