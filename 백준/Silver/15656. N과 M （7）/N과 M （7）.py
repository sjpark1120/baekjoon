import sys
n, m = map(int, sys.stdin.readline().split())
input = [0] * 10
input = list(map(int, sys.stdin.readline().split()))
input.sort()
arr = [0] * 10
used = [False] * 10
def nANDm(k):
    if k == m:
        for i in range(m):
            print(arr[i], end = ' ')
        print("")
        return 0
    else:
        for i in range(1, n+1):

                arr[k] = input[i-1]
                used[i] = True
                nANDm(k+1)
                used[i] = False
nANDm(0)