import sys
n, m = map(int, sys.stdin.readline().split())
input = [0] * 10
input = list(map(int, sys.stdin.readline().split()))
input.sort()
arr = [0] * 10
used = [False] * 10
def nANDm(k,a):
    if k == m:
        for i in range(m):
            print(arr[i], end = ' ')
        print("")
        return 0
    else:
        for i in range(a, n+1):
            if not used[i] and( k == 0 or arr[k-1] < input[i-1]):
                arr[k] = input[i-1]
                used[i] = True
                nANDm(k+1, a+1)
                used[i] = False
nANDm(0,1)