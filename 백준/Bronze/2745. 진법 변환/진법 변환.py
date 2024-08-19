import sys
n, b = map(str, sys.stdin.readline().split())
b = int(b)
anwser = 0
n = list(n)
n.reverse()
for i in range(len(n)):
  if n[i] >= 'A':
    anwser += (ord(n[i])-55) * b**i
  else:
    anwser += int(n[i]) * b**i
print(anwser)