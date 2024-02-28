def star(n, x, y):
  if(n == 3):
    arr[x][y] = '*'

    arr[x+1][y-1] = '*'
    arr[x+1][y+1] = '*'

    arr[x+2][y-2] = '*'
    arr[x+2][y-1] = '*'
    arr[x+2][y] = '*'
    arr[x+2][y+1] = '*'
    arr[x+2][y+2] = '*'
    return
  else:
    star(n//2, x, y)
    star(n//2, x+n//2, y- n//2)
    star(n//2, x+n//2, y + n//2)
n = int(input())
arr = [[' ']*(2*n-1) for i in range(n)]
star(n, 0, n-1)
for i in arr:
    print(''.join(i))