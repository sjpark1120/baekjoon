import sys
from collections import deque

def bfs(x, y):
    areacount = 1
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1 and visited[nx][ny] != 1:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    areacount += 1
    return areacount

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
n, m = map(int,sys.stdin.readline().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for j in range(m)] for i in range(n)]
count = 0
area = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visited[i][j] != 1:
            count +=1
            area = max(area, bfs(i,j))

print(count)
print(area)