import sys
n = int(sys.stdin.readline())
arr = [0]*1000001
arr2= [0]*1000001
for i in range(2, n+1):
    arr[i] = arr[i - 1] + 1
    arr2[i] = 1
    if i % 3 == 0:
        arr[i] = min(arr[i//3] + 1, arr[i])
        if(arr[i//3] + 1 == arr[i]):
          arr2[i] = 3
    if i % 2 == 0:
        arr[i] = min(arr[i//2] + 1, arr[i])
        if(arr[i//2] + 1 == arr[i]):
          arr2[i] = 2
print(arr[n])
print(n, end=" ")
while(1):
  if arr2[n] == 1:
    n -= 1
    print(n, end=" ")
  elif arr2[n] == 2:
    n //= 2
    print(n, end=" ")
  elif arr2[n] == 3:
    n //= 3
    print(n, end=" ")
  else:
     break