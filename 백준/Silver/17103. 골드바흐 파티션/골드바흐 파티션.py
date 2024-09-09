import sys
import math
def is_primenum(x):
  if x == 1 :
    return False
  for i in range (2, int(math.sqrt(x)) + 1):
    if x % i == 0:
      return False
  return True
list = [False] * 1000000
for i in range(1, 1000000):
  if is_primenum(i):
    list[i] = True
t = int(sys.stdin.readline())
for _ in range(t):
  n = int(sys.stdin.readline())
  num = 0
  for i in range(1,n//2+1):
    if list[n-i] and list[i]:
      num += 1
  print(num)