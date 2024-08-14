import sys
from collections import deque
n = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().split()))
line = deque(line)
another_line = []
check = 1
while(line or another_line):
  if len(line) > 0 and check == line[0]:
    line.popleft()
    check += 1
  elif len(another_line) > 0 and check == another_line[-1]:
    another_line.pop()
    check += 1
  elif len(line) > 0:
    another_line.append(line[0])
    line.popleft()

  if len(line) == 0 and len(another_line) > 0 and another_line[-1] != check:
    print("Sad")
    break
if len(line) == 0 and len(another_line) == 0:
  print("Nice")