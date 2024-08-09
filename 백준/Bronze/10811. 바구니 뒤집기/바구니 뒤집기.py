import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
for a in range(n):
  arr.append(a+1)
for _ in range(m):
  i, j = map(int, sys.stdin.readline().split())
  tmp = arr[i-1:j]
  for b in range(j-i+1):
    arr[j-b-1] = tmp[b]
for c in range(n):
  print(arr[c], end=' ')