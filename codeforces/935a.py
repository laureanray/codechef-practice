# https://codeforces.com/problemset/problem/935/A

def num_ways(n):
    count = 0
    for team_lead in range(1, n):
        member = n - team_lead
        if team_lead == 1 or member % team_lead == 0:
            count = count + 1

    return count

if __name__ == "__main__":  
    n = int(input())
    print(num_ways(n))