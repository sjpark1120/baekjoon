import sys
n = int(sys.stdin.readline())
rope = []
for i in range(n):
  rope.append(int(sys.stdin.readline()))
rope.sort()
max = 0
for i in range(n):
  if max < rope[i] * (n-i):
    max = rope[i] * (n-i)
print(max)