import sys

input = sys.stdin.readline

arr = list(input().strip())

height = 0

for i in range(len(arr)):
    if i == 0:
        height += 10
        continue
    if arr[i - 1] == arr[i]:
        height += 5
    else:
        height += 10
print(height)
