import sys
arr = []
for _ in range(3):
  n = int(sys.stdin.readline())
  arr.append(n)
if arr[0] == 60 and arr[1] == 60 and arr[2] == 60:
  print("Equilateral")
elif sum(arr) == 180:
  if arr[0] != arr[1] and arr[0] != arr[2] and arr[1] != arr[2]:
    print("Scalene")
  else:
    print("Isosceles")
else:
  print("Error")