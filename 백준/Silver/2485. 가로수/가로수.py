import sys
def gcd(x, y):
  while y > 0:
    x, y = y, x%y
  return x
n = int(sys.stdin.readline())
tree = []
loc = int(sys.stdin.readline())
first =loc
for _ in range(n-1):
  loc2 = int(sys.stdin.readline())
  tree.append(loc2-loc)
  loc = loc2
  if len(tree) == 2:
    x = gcd(tree[0], tree[1])
    tree = [x]
if n == 1:
  print(0)
elif (loc-first)%tree[0] > 0:
  print((loc-first)//tree[0] - n + 2)
else:
  print((loc-first)//tree[0] - n +1)