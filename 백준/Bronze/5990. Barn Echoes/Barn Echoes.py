import sys

input = sys.stdin.readline


a = list(input().rstrip())
b = list(input().rstrip())

maxlength = 0
limit = min(len(a), len(b))

for i in range(1, limit + 1):
    if a[-i:] == b[:i]:
        maxlength = max(maxlength, i)
for i in range(1, limit + 1):
    if b[-i:] == a[:i]:
        maxlength = max(maxlength, i)

print(maxlength)
