import sys
n = int(sys.stdin.readline())
arr = [[0 for _ in range(100)]for _ in range(100)]
count = 0

for _ in range(n):
  a, b = map(int, sys.stdin.readline().split()) 
  for i in range(a-1, a+9):
    for j in range(b-1, b+9):
      arr[i][j] = 1

for i in range(100):
  for j in range(100):
    if arr[i][j] == 1:
      count += 1
print(count)