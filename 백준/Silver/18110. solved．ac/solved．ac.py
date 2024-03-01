import math, sys
n = int(sys.stdin.readline())

if(n == 0):
  print(0)
else:
  arr = [0] * n
  check = math.floor(n*0.15+0.5)
  sum = 0

  for i in range(n):
    arr[i] = int(sys.stdin.readline())

  arr.sort()

  for i in range(check, n - check):
    sum += arr[i]

  average = math.floor(sum / (n - 2*check) + 0.5)
  print(average)