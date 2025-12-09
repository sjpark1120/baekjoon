import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

stack = []
rbn_arr = []

for num in reversed(arr):
    while stack and stack[-1] <= num:
        stack.pop()
    if not stack:
        rbn_arr.append(-1)
    else:
        rbn_arr.append(stack[-1])
    stack.append(num)

print(*reversed(rbn_arr))
