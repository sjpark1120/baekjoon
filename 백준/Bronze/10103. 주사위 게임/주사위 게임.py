import sys

input = sys.stdin.readline
changScore = 100
sangScore = 100
n = int(input())
for _ in range(n):
    c, s = map(int, input().split())
    if c > s:
        sangScore -= c
    elif s > c:
        changScore -= s

print(changScore)
print(sangScore)
