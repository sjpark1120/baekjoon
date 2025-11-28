import sys

input = sys.stdin.readline

n = int(input())
prize = []
for _ in range(n):
    f, s, t = map(int, input().split())
    if f == s == s == t:
        prize.append(10000 + f * 1000)
    elif f == s or s == t:
        prize.append(1000 + s * 100)
    elif t == f:
        prize.append(1000 + t * 100)
    else:
        prize.append(max([f, t, s]) * 100)

print(max(prize))
