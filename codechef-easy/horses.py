# https://www.codechef.com/problems/HORSES  

if __name__ == "__main__":
    for x in range(int(input())):
        n = int(input())
        S = list(map(int, input().split(' ')))
        S.sort()
        m = S[n-1] - S[n-2]
        for i in range(n-2, 0, -1):
            if S[i] - S[i-1] < m:
                m = S[i]-S[i-1]
        print(m)
