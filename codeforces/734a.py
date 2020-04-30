# https://codeforces.com/problemset/problem/734/A

if __name__ == "__main__":
    n = int(input())
    games = input()
    anton = 0
    danik = 0
    for c in games:
        if c == 'A':
            anton = anton + 1
        if c == 'D':
            danik = danik + 1

    if anton > danik:
        print('Anton')
    elif anton < danik:
        print('Danik')
    else:
        print('Friendship')