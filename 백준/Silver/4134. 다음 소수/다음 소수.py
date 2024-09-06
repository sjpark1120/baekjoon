import sys
import math
def is_primenum(x):
  for i in range (2, int(math.sqrt(x)) + 1):
    if x % i == 0:
      return False
  return True
n = int(sys.stdin.readline())
for _ in range(n):
  num = int(sys.stdin.readline())
  while(1):
    if num == 0 or num == 1:
      print(2)
      break
    if is_primenum(num):
      print(num)
      break
    num += 1