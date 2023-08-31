import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
arr = deque()
y = []
for i in range(n):
    arr.append(i+1)

while arr:
    arr.rotate(-(k-1))
    a = arr.popleft()
    y.append(a)

print("<", end = '')
for i in range(len(y)):
    if i == len(y)-1:
        print(y[i], end='')
    else:
        print("{},".format(y[i]), end=' ')

print(">")