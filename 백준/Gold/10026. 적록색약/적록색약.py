import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(a, b, check):
  q = deque()
  q.append((a, b))
  dis[a][b] = 1
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n and dis[nx][ny] == -1:
        if arr[nx][ny] == arr[x][y]:
          dis[nx][ny] = 1
          q.append((nx, ny))
        if check == 1:
          if (arr[nx][ny] == 'R' and arr[x][y] == 'G') or (arr[nx][ny] == 'G' and arr[x][y] == 'R'):
            dis[nx][ny] = 1
            q.append((nx, ny))

n = int(sys.stdin.readline())
arr = [list(map(str, list(sys.stdin.readline().strip()))) for _ in range(n)]
dis = [[-1 for _ in range(n)] for _ in range(n)]
count = 0
count_b = 0

for i in range(n):
  for j in range(n):
    if dis[i][j] == -1:
      bfs(i, j, 0)
      count += 1
print(count, end=' ')

dis = [[-1 for _ in range(n)] for _ in range(n)]
for i in range(n):
  for j in range(n):
    if dis[i][j] == -1:
      bfs(i, j, 1)
      count_b += 1
print(count_b)