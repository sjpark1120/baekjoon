import sys
a1, a0 = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
n0 = int(sys.stdin.readline())
check = 0
for n in range(n0, n0+101):
  if (a1-c)*n + a0 > 0:
    check = 1
if check == 0:
  print(1)
else:
  print(0)