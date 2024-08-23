import sys
word = []
for _ in range(5):
  input = str(sys.stdin.readline().rstrip())
  word.append(input)
for i in range(15):
  for j in range(5):
    if i < len(word[j]):
      print(word[j][i], end='')