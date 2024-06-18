import sys
sys.setrecursionlimit(10**9)
def dfs(r):
  global cnt
  visited[r] =cnt
  line[r].sort(reverse=True) # 내림차순으로 정렬
  for i in line[r]:
    if visited[i] == 0:
      cnt +=1
      dfs(i)

n,m,r = map(int, sys.stdin.readline().split())
visited = [0] * (n+1)
line = [[] for _ in range(n+1)]
cnt = 1
for i in range(m):
  u, v = map(int, sys.stdin.readline().split())
  line[u].append(v)
  line[v].append(u)
dfs(r)
for i in range(1, n+1):
  print(visited[i])