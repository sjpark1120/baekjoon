import sys

def func(k):
  global vowel, consonant
  if k == 0:
    vowel =0
    consonant = 0
  if k == l and vowel>0 and consonant >1:
    for i in range(l):
      print(password[i], end = '')
    print('')
    return 0 
  for i in range(c):
    if not isused[i] and (k == 0 or password[k-1] < c_list[i]):
      if c_list[i] in vowels:
        vowel += 1
      else:
        consonant += 1
      password[k] = c_list[i]
      isused[i] = True
      func(k+1)
      if c_list[i] in vowels:
        vowel -= 1
      else:
        consonant -= 1
      isused[i] = False

l, c = map(int, sys.stdin.readline().split())
c_list = list(map(str, sys.stdin.readline().split()))
c_list.sort()
vowels = ['a', 'e', 'i', 'o', 'u']
password = [0] * 15
isused = [False] * 15
vowel =0
consonant = 0
func(0)