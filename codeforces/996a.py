if __name__ == "__main__":
    n = int(input())
 
    bills = 0

    if n > 100:
        bills = n // 100
        n = n - (n // 100 * 100)

    if n // 20 > 0:
        bills = bills + n // 20
        n = n - (n // 20 * 20)

    if n // 10 > 0:
        bills = bills + n // 10
        n = n - (n // 10 * 10)

    if n // 5 > 0:
        bills = bills + n // 5
        n = n - (n // 5 * 5)

    if n // 1 > 0:
        bills = bills + n
        n = n - ( n // 1 * 1)

    print(bills)