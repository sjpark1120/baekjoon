import sys
from collections import deque
n= int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[0]*(n+1) for _ in range(n+1)]
visited = [False]*(n+1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

def bfs(v):
    visited[v] = True
    q = deque()
    q.append(v)
    global num
    num = 0
    while q:
        k = q.popleft()
        num += 1
        for w in range(len(graph[v])):
            if graph[k][w] == 1 and visited[w] == False:
                visited[w] = True
                q.append(w)
bfs(1)
print(num-1)
