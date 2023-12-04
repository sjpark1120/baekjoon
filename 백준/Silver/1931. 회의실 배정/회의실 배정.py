import sys
n = int(sys.stdin.readline())
time = [[0]*2 for _ in range(n)]
for i in range(n):
  start, end = map(int, sys.stdin.readline().split())
  time[i][0] = start
  time[i][1] = end

time.sort(key = lambda x:(x[1], x[0]))


e = 0
cnt = 0
for i in range(n):
  if  e <= time[i][0]:
    e = time[i][1]
    cnt += 1
print(cnt)