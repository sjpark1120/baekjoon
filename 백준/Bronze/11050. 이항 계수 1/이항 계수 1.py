import sys
n, k = map(int, sys.stdin.readline().split())

def fuc1(a, b):
    if a == 0 or b == 0:
        return 1
    return a*fuc1(a-1, b-1)/b
print(int(fuc1(n,k)))
