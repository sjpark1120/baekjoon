import sys

input = sys.stdin.readline

n = int(input())
stack = []
score = 0

for _ in range(n):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        stack.append([arr[1], arr[2]])
    if len(stack) == 0:
        continue
    stack[-1][1] -= 1
    if stack[-1][1] == 0:
        p = stack.pop()
        score += p[0]
print(score)
