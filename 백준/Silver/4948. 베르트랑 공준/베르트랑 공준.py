import math
def primenum(m, n):
    array = [True]*(n+1)
    array[1] = False
    count = 0
    for i in range(2, int(math.sqrt(n))+1):
        if array[i]:
            j = 2
            while i*j <= n:
                array[i*j] = False
                j += 1
    for i in range(m, n+1):
        if array[i]:
            count += 1
    return count

while(True):
    k = int(input())
    if k == 0:
        break

    print(primenum(k+1, 2*k))