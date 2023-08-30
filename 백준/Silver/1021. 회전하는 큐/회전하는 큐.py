from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())
deque = deque()
cnt = 0
for i in range(n):
    deque.append(i+1)
arr = list(map(int, sys.stdin.readline().split()))
for i in arr:
    x = 0
    while deque[0] != i:
        deque.append(deque.popleft())
        x += 1
    if x > len(deque)/2:
        x = len(deque) - x
    deque.popleft()
    cnt += x
print(cnt)