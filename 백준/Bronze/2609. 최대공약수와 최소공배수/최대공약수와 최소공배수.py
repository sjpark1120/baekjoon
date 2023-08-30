import sys
a, b = map(int, sys.stdin.readline().split())
def gcd(a,b):
    if a%b ==0:
        return b
    else:
        return gcd(b, a%b)
print(gcd(a,b))
print(int(a*b/gcd(a,b)))