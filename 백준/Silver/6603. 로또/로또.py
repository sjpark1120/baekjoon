def func(x):
  global a
  if x == 6:
    for i in range(6):
      print(anwser[i], end=' ')
    print()
    return
  else:
    if x == 0:
      a = 1
    for i in range(a, arr[0]+1):
      if not isused[i]:
        anwser[x] = arr[i]
        isused[i] = True
        a = i
        func(x+1)
        isused[i] = False

while True:
  arr = list(map(int, input().split()))
  if(arr[0] == 0):
    break
  anwser = [0] * 6
  isused = [False] * (arr[0]+1)
  func(0)
  print()