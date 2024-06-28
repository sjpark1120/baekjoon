import sys

def nandm(k):
  if k == m:
    for i in range(m):
      print(arr[i], end = ' ')
    print('')
    return 0 
  for i in range(1, n+1):
    if k == 0 or arr[k-1] <= i:
      arr[k] = i
      nandm(k+1)

n, m = map(int, sys.stdin.readline().split())
arr = [0] * 10
isused = [False] * 10
nandm(0)