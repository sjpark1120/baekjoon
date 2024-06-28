import sys

def nandm(k):
  if k == m:
    for i in range(m):
      print(arr[i], end = ' ')
    print('')
    return 0 
  for i in range(n):
    if not isused[i]:
      arr[k] = n_list[i]
      isused[i] =True
      nandm(k+1)
      isused[i] = False

n, m = map(int, sys.stdin.readline().split())
n_list = list(map(int, sys.stdin.readline().split()))
n_list.sort()
arr = [0] * 10
isused = [False] * 10
nandm(0)