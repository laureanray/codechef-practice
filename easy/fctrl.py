n = int(input())

def z(n):
    res = n // 5
    if res < 5:
        return res
    else:
        return res + z(res)


for i in range(n):
    factorial = int(input())
    print(z(factorial))