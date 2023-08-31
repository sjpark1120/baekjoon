import sys
n, k = map(int, sys.stdin.readline().split())
v = [0]*(n+1)
w = [0]*(n+1)
m = [[0 for j in range(k+1)] for i in range(n+1)]
for i in range(1, n+1):
    w[i], v[i] = map(int, sys.stdin.readline().split())

for i in range(1, n+1):
    for j in range(1, k+1):
        if w[i] > j:
            m[i][j] = m[i-1][j]
        else:
            m[i][j] = max(m[i-1][j], v[i]+m[i-1][j-w[i]])
print(m[n][k])
