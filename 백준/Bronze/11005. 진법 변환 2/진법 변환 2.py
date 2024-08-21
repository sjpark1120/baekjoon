import sys
n, b = map(int, sys.stdin.readline().split())
anwser = []
while(n):
  anwser.append(n%b)
  n = n//b
anwser.reverse()
for i in anwser:
  if i > 9:
    print(chr(i+55), end='')
  else:
    print(i, end='')