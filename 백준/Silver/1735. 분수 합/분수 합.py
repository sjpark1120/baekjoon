import sys
def gcd(x, y):
  while y > 0:
    x, y = y, x%y
  return x
ass, amm = map(int, sys.stdin.readline().split())
bss, bmm = map(int, sys.stdin.readline().split())
answers = ass*bmm + bss*amm
answerm = amm * bmm
g = gcd(answers, answerm)
print(answers//g, answerm//g)