import sys
a, b, c = map(int, sys.stdin.readline().split())
if a >= b >= c or c >= b >= a:
    print(b)
elif b >= a >= c or c >= a >= b:
    print(a)
elif a >= c >= b or b >= c >= a:
    print(c)
