# https://www.codechef.com/problems/CIELAB
    
if __name__ == "__main__":
    (a, b) = map(int, input().split(' '))
    ans = str(a - b)
    ans = list(ans)
    
    if len(ans) == 1:
        i = 0
    else:
        i = len(ans) - 1

    if int(ans[i]) < 9:
        ans[i] = str(int(ans[i]) + 1)
    else:
        ans[i] = str(int(ans[i]) - 1)
    a = ""
    print(a.join(ans))        
    