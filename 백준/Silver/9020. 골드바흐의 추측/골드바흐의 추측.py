import sys
import math
def primenum(m, n):
    array = [True]*(n+1)
    array[1] = False
    count = 0
    a = [0]*(n-m)
    for i in range(2, int(math.sqrt(n))+1):
        if array[i]:
            j = 2
            while i*j <= n:
                array[i*j] = False
                j += 1
    return array

t = int(sys.stdin.readline())
arr = primenum(1, 10001)
for i in range(t):
    n = int(sys.stdin.readline())
    for j in range(n//2, n):
        if arr[j] == True and arr[n-j] == True:
            print("{} {}".format(n-j, j))
            break