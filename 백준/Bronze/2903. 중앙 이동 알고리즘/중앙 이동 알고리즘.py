import sys
n = int(sys.stdin.readline())

def func(x):
  if x == 1:
    return 3
  return func(x-1) + (2**(x-1))
print(func(n)**2)