import sys
from collections import deque
n, m, v = map(int, sys.stdin.readline().split())
graph = [[0]*(n+1) for _ in range(n+1)]
visited = [False]*(n+1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in range(len(graph[v])):
        if graph[v][i] == 1 and visited[i] == False:
            dfs(i)
def bfs(v):
    visited[v] = True
    q = deque()
    q.append(v)
    while q:
        k = q.popleft()
        print(k, end=' ')
        for w in range(len(graph[v])):
            if graph[k][w] == 1 and visited[w] == False:
                visited[w] = True
                q.append(w)
dfs(v)
visited = [False]*(n+1)
print()
bfs(v)
