import sys
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
prefixSum = [0]*(n+1)
prefixSum[0] = 0
for i in range(1, n+1):
  prefixSum[i] = prefixSum[i-1] + arr[i-1]
for a in range(m):
  i, j = map(int, sys.stdin.readline().split())
  sum = prefixSum[j] - prefixSum[i-1]
  print(sum)