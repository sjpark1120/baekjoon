import sys
from collections import deque
n = int(sys.stdin.readline())
deck = []
deck = deque(deck)
for _ in range(n):
  command = list(map(int, sys.stdin.readline().split()))
  if command[0] == 1:
    deck.appendleft(command[1])
  if command[0] == 2:
    deck.append(command[1])
  elif command[0] == 3:
    if deck:
      print(deck.popleft())
    else:
      print(-1)  
  elif command[0] == 4:
    if deck:
      print(deck.pop())
    else:
      print(-1)
  elif command[0] == 5:
    print(len(deck))
  elif command[0] == 6:
    if deck:
      print(0)
    else:
      print(1)
  elif command[0] == 7:
    if(deck):
      print(deck[0])
    else:
      print(-1)
  elif command[0] == 8:
    if(deck):
      print(deck[-1])
    else:
      print(-1)