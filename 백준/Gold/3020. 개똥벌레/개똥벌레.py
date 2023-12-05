import sys
from bisect import bisect_left
n, h = map(int, sys.stdin.readline().split())
jong = []
suk = []
check = 0
for i in range(n):
  size = int(sys.stdin.readline())
  if check == 0:
    suk.append(size)
    check = 1
  elif check == 1:
    jong.append(size)
    check = 0
jong.sort()
suk.sort()
min = 200000
cnt = 0
for i in range(1, h+1):
  j = bisect_left(jong, h+1-i)
  s = bisect_left(suk, i)
  if min > n-j-s:
    min = n-j-s
    cnt = 1
  elif min == n-j-s:
    cnt += 1
print(min, cnt)