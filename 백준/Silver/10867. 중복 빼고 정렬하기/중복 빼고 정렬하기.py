import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
result = []
for i in range(n):
    if arr[i] not in result:
        result.append(arr[i])
for i in range(len(result)):
    print(result[i], end=' ')