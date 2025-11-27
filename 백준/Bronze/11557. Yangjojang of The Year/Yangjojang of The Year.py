import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    maxS, maxL = '', -1
    for _ in range(n):
        s, l = input().split()
        l = int(l)
        if maxL < l:
            maxS, maxL = s, l
    print(maxS)