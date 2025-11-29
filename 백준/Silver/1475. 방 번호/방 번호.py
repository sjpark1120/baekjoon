import sys

input = sys.stdin.readline

arr = list(input().strip())
counts = [0] * 9
for i in arr:
    if i == "9":
        counts[6] += 1
    else:
        counts[int(i)] += 1
counts[6] = (counts[6] + 1) // 2

print(max(counts))
