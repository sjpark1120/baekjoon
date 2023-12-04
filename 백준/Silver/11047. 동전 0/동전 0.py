import sys
n, k = map(int, sys.stdin.readline().split())
coin = []
count = 0
for i in range(n):
  coin.append(int(sys.stdin.readline()))
for i in range(n):
  count = count + k // coin[n-1-i]
  k = k % coin[n-1-i]
print(count)