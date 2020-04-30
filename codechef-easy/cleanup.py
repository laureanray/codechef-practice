def solve(completed, must_be_completed, list_jobs_completed):
    missing = []
    for i in range(must_be_completed):
        q = i + 1
        if q not in list_jobs_completed:
            missing.append(q)

    # chef
    remain = must_be_completed - completed
    
    chef = []
    staff = []

    for i in range(remain):
        if i % 2 == 0:
            chef.append(missing[i])
        else:
            staff.append(missing[i])
    
    return chef, staff

if __name__ == "__main__":

    try:
        T = int(input())
        results = []

        for i in range(T):
            n, m = map(int, input().split())
            l = list(map(int, input().split()))
            results.append(solve(m, n, l))

        for chef, staff in results:
            print(*chef, sep=" ")
            print(*staff, sep=" ")

    except:
        pass

