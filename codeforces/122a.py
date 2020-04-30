# https://codeforces.com/problemset/problem/122/A

def find_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)

    return factors

def has4or7(n):
    ns = str(n)

    if n % 7 == 0 or n % 4 == 0:
        return True
    else:
        if all (c in '47' for c in ns):
            return True
    return False
    
def is_lucky(n):
    if has4or7(n):
        return 'YES'
    else:
        for factor in find_factors(n):
            if has4or7(factor):
                return 'YES'
        else:
            return 'NO'


if __name__ == "__main__":
    n = int(input())
    print(is_lucky(n))    
    # print(find_factors(n))