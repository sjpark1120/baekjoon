from collections import deque
import sys
       
n, m  = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    u, v  = map(int, sys.stdin.readline().split())
    graph[u].append(v)  
    graph[v].append(u)  
visited = [False] * (n+1)
cnt = 0

for i in range(1, n+1):
    if visited[i] == True: 
        continue
    queue = deque([i])
    visited[i] = True
    
    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
    cnt+= 1
print(cnt)