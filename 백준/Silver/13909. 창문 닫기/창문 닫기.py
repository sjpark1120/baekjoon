import sys
n = int(sys.stdin.readline())
count = 1
while(True):
  if count**2 <= n:
    count += 1
  else:
    break
print(count-1)