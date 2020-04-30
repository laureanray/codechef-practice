if __name__ == "__main__":
    res = 0
    N = int(input())
    for i in range(N):
        a = input()
        if a == 'Tetrahedron':
            res = res + 4
        elif a == 'Cube':
            res = res + 6
        elif a == 'Octahedron':
            res = res + 8
        elif a == 'Dodecahedron':
            res = res + 12
        elif a == 'Icosahedron':
            res = res + 20
    print(res)      