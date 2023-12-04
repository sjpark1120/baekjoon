import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
a.sort()
b.sort(reverse=True)
cnt = 0
for i in range(n):
  cnt += a[i] * b[i]
print(cnt)