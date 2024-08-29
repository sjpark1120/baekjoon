import sys
a,b,c = map(int, sys.stdin.readline().split())
if max(a,b,c)*2 < a+b+c:
  print(a+b+c)
else:
  print(2*(a+b+c-max(a,b,c))-1)