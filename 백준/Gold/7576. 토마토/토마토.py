import sys
from collections import deque

def bfs():
#    q = deque()
#   q.append((x, y))
#   dis[x][y] = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0 and dis[nx][ny] == -1:
                    dis[nx][ny] = dis[x][y]+1
                    q.append((nx, ny))
    return

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
m, n = map(int,sys.stdin.readline().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dis = [[-1 for j in range(m)] for i in range(n)]
q = deque()
count = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i, j))
            dis[i][j] = 0
        elif arr[i][j] == -1:
            dis[i][j] = -2
bfs()

for i in range(n):
    for j in range(m):
        if dis[i][j] == -1:
            print(-1)
            exit()
        count = max(count, dis[i][j])

print(count)
