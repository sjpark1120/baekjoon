import sys
word = list(sys.stdin.readline().strip())
word_r = list(reversed(word))
if word == word_r:
  print(1)
else:
  print(0)