import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
for a in range(n):
  arr.append(a+1)
for _ in range(m):
  i, j = map(int, sys.stdin.readline().split())
  tmp = arr[i-1]
  arr[i-1] = arr[j-1]
  arr[j-1] = tmp
for a in range(n):
  print(arr[a], end=' ')