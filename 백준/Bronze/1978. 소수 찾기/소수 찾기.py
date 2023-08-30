def prime(x):
    if x == 1:
        return False
    for j in range(2, num[i]):
        if x % j == 0:
            return False
    return True
n = int(input())
primenum = 0
num = list(map(int, input().split()))
for i in range(n):
    if prime(num[i]):
        primenum += 1
print(primenum)