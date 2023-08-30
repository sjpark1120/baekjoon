import sys
n = int(sys.stdin.readline())
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)
m = factorial(n)
a = 0
while(m % 10 == 0):
    m = m // 10
    a += 1
print(a)