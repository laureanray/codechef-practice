n = 10
m = 12
q = 14

s = ['a', 'b', 'c']
t = ['c', 'd', 'e', 'f', 'g']

for i in range(q):

    print(i, s[i % len(s)], t[i % len(t)])