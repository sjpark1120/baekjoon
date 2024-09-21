import sys
from collections import deque
n = int(sys.stdin.readline())
arr_a = list(map(int, sys.stdin.readline().split()))
arr_b = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr_c = list(map(int, sys.stdin.readline().split()))
arr = deque()
for i in range(n):
  if arr_a[i] == 0:
    arr.append(arr_b[i])
for i in range(m):
  arr.appendleft(arr_c[i])
for i in range(m):
  print(arr.pop(),end=' ')