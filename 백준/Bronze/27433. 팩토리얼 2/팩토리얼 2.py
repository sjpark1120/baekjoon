import sys
def factorial(x):
  if x == 0:
    return 1
  if x == 1:
    return x
  return x * factorial(x-1)

n = int(sys.stdin.readline())
print(factorial(n))