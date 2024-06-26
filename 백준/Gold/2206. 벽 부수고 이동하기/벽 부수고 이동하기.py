import sys
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs():
  q = deque()
  q.append((0, 0, 0)) # x, y, 벽 파괴 여부
  dist[0][0][0] = 1
  while q:
    x, y, z = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        if map[nx][ny] == 1 and z == 0:
          nz = 1
          if dist[nx][ny][nz] == inf:
            dist[nx][ny][nz] = dist[x][y][z] +1
            q.append((nx, ny, nz))
        if map[nx][ny] == 0:
          nz = z
          if dist[nx][ny][nz] == inf:
            dist[nx][ny][nz] = dist[x][y][z]+1
            q.append((nx, ny, nz))

inf = float('inf')
n, m = map(int, sys.stdin.readline().split())
map = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
dist = [[[inf for _ in range(2)] for _ in range(m)] for _ in range(n)]
bfs()
min_path = min(dist[n-1][m-1][0], dist[n-1][m-1][1])
if min_path == inf:
  print(-1)
else:
  print(min_path)