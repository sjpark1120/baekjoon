dx = [-1,1,0,0]
dy = [0,0,-1,1]
def BFS(x,y):
  queue = [(x,y)]
  matrix[x][y] = 0 #방문
  while queue:
    x,y = queue.pop(0)
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= m or ny < 0 or ny >= n:
        continue
      if matrix[nx][ny] == 1:
        queue.append((nx, ny))
        matrix[nx][ny] = 0
import sys
t = int(sys.stdin.readline())
for i in range(t):
  m, n, k = map(int, sys.stdin.readline().split())
  matrix = [[0]*(n) for _ in range(m)]
  count = 0
  for j in range(k):
    x, y = map(int, sys.stdin.readline().split())
    matrix[x][y] = 1
  for a in range(m):
    for b in range(n):
      if matrix[a][b] == 1:
        BFS(a,b)
        count += 1
  print(count)