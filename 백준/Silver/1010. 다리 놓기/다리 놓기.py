import sys
n = int(sys.stdin.readline())

def func1(a, b):
    if b == 0:
        return 1
    return a * func1(a - 1, b - 1) // b

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(func1(b, b-a))
