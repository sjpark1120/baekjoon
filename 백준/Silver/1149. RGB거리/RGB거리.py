import sys
n = int(sys.stdin.readline())
cost = [[]] * n
D = [[0 for _ in range(3)]for _ in range(n)]

for i in range(n):
  cost[i] = list(map(int, sys.stdin.readline().split()))

D[0][0] = cost[0][0]
D[0][1] = cost[0][1]
D[0][2] = cost[0][2]

for i in range(1, n):
  D[i][0] = min(D[i-1][1]+cost[i][0], D[i-1][2]+cost[i][0])
  D[i][1] = min(D[i-1][0]+cost[i][1], D[i-1][2]+cost[i][1])
  D[i][2] = min(D[i-1][1]+cost[i][2], D[i-1][0]+cost[i][2])
print(min(D[n-1]))