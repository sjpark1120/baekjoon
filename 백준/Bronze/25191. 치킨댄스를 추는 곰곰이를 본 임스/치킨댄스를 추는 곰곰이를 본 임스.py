import sys
n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
num = a//2+b
if num > n:
    print(n)
else:
    print(num)