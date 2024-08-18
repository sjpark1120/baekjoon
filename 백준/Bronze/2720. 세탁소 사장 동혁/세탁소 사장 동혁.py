import sys
t = int(sys.stdin.readline())
for _ in range(t):
  c = int(sys.stdin.readline())
  quarter = int(c // 25)
  c = c % 25
  print(quarter, end=' ')
  dime = int(c // 10)
  c = c % 10
  print(dime, end=' ')
  nickel = int(c // 5)
  c = c % 5
  print(nickel, end=' ')
  penny = int(c // 1)
  c = c % 1
  print(penny, end=' ')
  print('')