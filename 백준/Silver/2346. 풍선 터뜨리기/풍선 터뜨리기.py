import sys
from collections import deque
n = int(sys.stdin.readline())
queue = deque(list(i+1 for i in range(n)))
arr = list(map(int, sys.stdin.readline().split()))
tmp = queue.popleft()
print(tmp, end=' ')
while(queue):
  if arr[tmp-1] > 0:
    queue.rotate(-arr[tmp-1]+1)
  else:
    queue.rotate(-arr[tmp-1])
  tmp = queue.popleft()
  print(tmp,end=' ')