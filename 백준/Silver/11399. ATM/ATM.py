import sys
n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
p.sort()
time = 0
for i in range(n):
  for j in range(i+1):
    time += p[j]
print(time)