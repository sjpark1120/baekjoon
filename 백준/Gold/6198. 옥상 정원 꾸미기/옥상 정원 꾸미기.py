import sys

input = sys.stdin.readline

n = int(input())
arr = []

stack = []
sum_all = []

for _ in range(n):
    b_height = int(input())
    arr.append(b_height)

for h in reversed(arr):
    count = 0
    while stack:
        if stack[-1][0] >= h:
            stack.append([h, count])
            break
        else:
            count += stack.pop()[1] + 1

    if not stack:
        stack.append([h, count])

    sum_all.append(count)

print(sum(sum_all))
