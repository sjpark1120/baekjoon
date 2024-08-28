import sys
n = int(sys.stdin.readline())
max_x = -10000
max_y = -10000
min_x = 10000
min_y = 10000
for _ in range(n):
  x, y = map(int, sys.stdin.readline().split())
  if x > max_x:
    max_x = x
  if y > max_y:
    max_y = y
  if x < min_x:
    min_x = x
  if y < min_y:
    min_y = y
print((max_x-min_x)*(max_y-min_y))