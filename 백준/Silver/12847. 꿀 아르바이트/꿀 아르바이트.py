import sys
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
prefixSum = [0]*(n)
prefixSum[0] = arr[0]
for i in range(1, n):
  prefixSum[i] = prefixSum[i-1] + arr[i]
max = prefixSum[m-1]
for a in range(n-m):
  if max < prefixSum[a+m] - prefixSum[a]:
    max = prefixSum[a+m] - prefixSum[a]
print(max)