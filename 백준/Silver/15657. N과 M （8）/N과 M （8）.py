import sys

def nandm(k):
  if k == m:
    for i in range(m):
      print(arr[i], end = ' ')
    print('')
    return 0 
  for i in range(n):
      if k == 0 or arr[k-1] <= n_list[i]:
        arr[k] = n_list[i]
        nandm(k+1)

n, m = map(int, sys.stdin.readline().split())
n_list = list(map(int, sys.stdin.readline().split()))
n_list.sort()
arr = [0] * 10
nandm(0)