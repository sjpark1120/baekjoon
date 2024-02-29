def func(s, t):
  global check
  if(check == 1):
    return
  if(len(s) == len(t)):
    if (s == t):
      check =1
    return
  else:
    if(t[-1] == "A"):
      func(s, t[:-1])
    if(t[0] == "B"):
      func(s, t[:0:-1])



s = list(input())
t = list(input())
check =0
func(s, t)
print(check)