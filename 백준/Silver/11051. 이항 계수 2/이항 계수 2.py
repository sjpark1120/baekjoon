import sys
n, k = map(int, sys.stdin.readline().split())
arr = [[1 for col in range(k+1)] for row in range(n+1)]
for i in range(2, n+1):
    for j in range(1, k+1):
        arr[i][j] = arr[i-1][j-1] * i // j
print(arr[n][k]%10007)