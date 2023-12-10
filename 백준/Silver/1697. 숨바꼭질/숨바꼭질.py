from collections import deque
import sys
def BFS(x, y):
  deq = deque()
  deq.append(x)
  while deq:
    v = deq.popleft()
    arr = [v-1, v+1, v*2]
    if v == y:
      return cnt[v]
    for i in arr:
      if 0 <= i <= 10**5 and not cnt[i]:
        cnt[i] = cnt[v] +1
        deq.append(i)
n, k = map(int, sys.stdin.readline().split())
cnt = [0] * (10**5+1)
print(BFS(n, k))