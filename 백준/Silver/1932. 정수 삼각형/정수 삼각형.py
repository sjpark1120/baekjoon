import sys
from collections import deque

input = sys.stdin.readline

a = []
b = []

n = int(input())

for i in range(n):
    numbers = list(map(int, input().split()))
    a.append(numbers)

    dp_row = []
    for j in range(i + 1):
        if i == 0:
            dp_row.append(a[i][j])
        elif j == 0:
            dp_row.append(b[i - 1][j] + a[i][j])
        elif j == i:
            dp_row.append(b[i - 1][j - 1] + a[i][j])
        else:
            dp_row.append(max(b[i - 1][j - 1], b[i - 1][j]) + a[i][j])
    b.append(dp_row)

print(max(b[-1]))
