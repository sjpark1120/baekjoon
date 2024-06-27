import sys
from collections import deque
sys.setrecursionlimit(10**9)
def dfs(i):
  global count
  visited[i] = True
  team.append(i)
  next = arr[i]
  if visited[next]:
    if next in team:
      t_index = team.index(next)
      count += len(team[t_index:])
  else:
    dfs(next)


t = int(sys.stdin.readline())
for i in range(t):
  n = int(sys.stdin.readline())
  arr = [0] + list(map(int, sys.stdin.readline().split()))
  count = 0
  visited = [False for _ in range(n+1)]
  for j in range(1, n+1):
    if not visited[j]:
      team = []
      dfs(j)
  print(n - count)