import sys
from collections import deque
n = int(sys.stdin.readline())
arr = deque()
for i in range(n):
    arr.append(i+1)
while len(arr) > 1:
    arr.popleft()
    k = arr.popleft()
    arr.append(k)
print(arr[0])