import sys
n = int(sys.stdin.readline())
arr = [0 for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, sys.stdin.readline().split()))

arr.sort(key = lambda x: (x[1], x[0]))

for i in range(n):
    print(arr[i][0], arr[i][1])
