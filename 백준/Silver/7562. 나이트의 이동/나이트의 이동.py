import sys
from collections import deque

dx = [-1, -2, 1, 2, -1, -2, 1, 2]
dy = [2, 1, 2, 1, -2, -1, -2, -1]

def knight(fx,fy,gx,gy):
  if fx == gx and fy == gy:
    return 0
  q = deque()
  q.append((fx,fy))
  chess[fx][fy] = 0
  while q:
    x, y = q.popleft()
    for j in range(8):
      nx = x + dx[j]
      ny = y + dy[j]
      if 0 <= nx < i and 0 <= ny < i:
        if nx == gx and ny == gy:
          return chess[x][y] + 1
        if chess[nx][ny] == -1:
          q.append((nx, ny))
          chess[nx][ny] = chess[x][y] + 1

n = int(sys.stdin.readline())
for _ in range(n):
  i = int(sys.stdin.readline())
  first_x, first_y = map(int, sys.stdin.readline().split()) 
  goal_x, goal_y = map(int, sys.stdin.readline().split()) 
  chess = [[-1 for _ in range(i)] for _ in range(i)]
  print(knight(first_x, first_y, goal_x, goal_y))