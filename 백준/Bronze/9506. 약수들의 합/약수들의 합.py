import sys
while(1):
  n = int(sys.stdin.readline())
  if n == -1:
    break
  arr = []

  for i in range(1, n+1):
    if n % i == 0:
      arr.append(i)
  
  arr.pop()
  if sum(arr) == n:
    print(n, "=", end=' ')
    for i in arr:
      print(i, end=' ')
      if i != arr[-1]:
        print("+", end=' ')
      else:
        print('')
  else:
    print(n, "is NOT perfect.")