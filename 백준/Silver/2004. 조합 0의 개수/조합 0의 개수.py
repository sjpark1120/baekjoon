import sys
import math
n, m = map(int, sys.stdin.readline().split())
def countnumber(i, j):
    count = 0
    while i:
        i //= j
        count += i
    return count

countfive = countnumber(n, 5) - countnumber(m, 5) - countnumber(n-m, 5)
counttwo = countnumber(n, 2) - countnumber(m, 2) - countnumber(n-m, 2)

print(min(countfive, counttwo))