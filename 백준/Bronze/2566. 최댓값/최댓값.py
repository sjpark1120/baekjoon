import sys
maxNum = 0
maxLoc = [1,1]
for i in range(9):
  arr = list(map(int, sys.stdin.readline().split()))
  for j in range(9):
    if maxNum < arr[j]:
      maxNum = arr[j]
      maxLoc = [i+1, j+1]
print(maxNum)
print(maxLoc[0], maxLoc[1])