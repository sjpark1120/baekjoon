import sys
from collections import deque

# 방향 벡터 (상, 하, 좌, 우, 위, 아래)
dx = [1, 0, -1, 0, 0, 0]
dy =[0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

m, n, h = map(int, sys.stdin.readline().split())
arrs = []
for _ in range(h):
  arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
  arrs.append(arr)
q = deque()
for z in range(h):
  for y in range(n):
    for x in range(m):
      if arrs[z][y][x] == 1:
        q.append((z, y, x))

def bfs():
  while q:
    z, y, x = q.popleft()
    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]
      if 0 <= nx < m and 0 <= ny < n and 0 <= nz <h:
        if arrs[nz][ny][nx] == 0:
          arrs[nz][ny][nx] =  arrs[z][y][x] + 1
          q.append((nz,ny,nx))

bfs()
max_day = 0
for x in range(m):
  for y in range(n):
    for z in range(h):
      if arrs[z][y][x] == 0:
        print(-1)
        exit(0)
      max_day = max(max_day, arrs[z][y][x])

print(max_day-1)