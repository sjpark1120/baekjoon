n, m =map(int, input().split())
a = [0]*n
b = [0]*n
c = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
for i in range(n):
    b[i] = list(map(int, input().split()))
for i in range(n):
    for j in range(m):
        c[i][j] = a[i][j] + b[i][j]
        print(c[i][j], end=" ")
    print()