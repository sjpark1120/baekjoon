import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
t = int(input())
hands = deque(list(map(int, input().split())))
numbers = list(map(int, input().split()))

for i in range(t):
    for j in range(numbers[i] - 1):
        hand = hands.popleft()
        hands.append(hand)
    print(hands[0], end=" ")