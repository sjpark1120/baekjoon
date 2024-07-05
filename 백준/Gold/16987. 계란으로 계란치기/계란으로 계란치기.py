import sys

# h = 손에든 계란 번호
def egg(h):
  global mx, count
  if h == n:
    mx = max(mx, count)
    return 
  if s_arr[h] <= 0 or count == n-1:
    egg(h+1)
    return
  for i in range(n):
    if s_arr[i]>0 and h != i:
      s_arr[i] -= w_arr[h]
      s_arr[h] -= w_arr[i]
      if s_arr[i] <= 0:
        count += 1
      if s_arr[h] <= 0:
        count += 1
      egg(h+1)
      if s_arr[i] <= 0:
        count -= 1
      if s_arr[h] <= 0:
        count -= 1
      s_arr[i] += w_arr[h]
      s_arr[h] += w_arr[i]

n = int(sys.stdin.readline())
s_arr = []
w_arr = []
count =0
mx = 0
for i in range(n):
  s, w = map(int, sys.stdin.readline().split())
  s_arr.append(s)
  w_arr.append(w)
egg(0)
print(mx)