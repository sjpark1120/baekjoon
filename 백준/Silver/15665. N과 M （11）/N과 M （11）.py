import sys
n, m = map(int, sys.stdin.readline().split())
input = list(map(int, sys.stdin.readline().split()))
input.sort()
arr = []
used = [False] * 10

def nANDm(k):
    if k == m:
        for i in range(m):
            print(arr[i], end = ' ')
        print("")
        return 0
    else:
        overlap = 0
        for i in range(n):
            if overlap != input[i]:
                arr.append(input[i])
                overlap = input[i]
                used[i] = True
                nANDm(k+1)
                used[i] = False
                arr.pop()
nANDm(0)