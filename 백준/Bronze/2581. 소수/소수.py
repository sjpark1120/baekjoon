def prime(x):
    if x == 1:
        return False
    for j in range(2, x):
        if x % j == 0:
            return False
    return True
primenum = 0
primesmall = 10001
n = int(input())
m = int(input())
for i in range(n,m+1):
    if prime(i):
        primenum += i
        if primesmall > i:
            primesmall = i
if primesmall == 10001:
    print(-1)
else:
    print(primenum)
    print(primesmall)