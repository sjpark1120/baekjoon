import sys
from collections import Counter
n = int(sys.stdin.readline())
list_n = [0] * n
sum = 0
for i in range(n):
    list_n[i] = int(sys.stdin.readline())
    sum += list_n[i]
small = list_n[0]
big = list_n[0]
for i in range(n):
    if small > list_n[i]:
        small = list_n[i]
    if big < list_n[i]:
        big = list_n[i]
list_n.sort()
if (n == 1):
    modesec = list_n[0]
else:
    mode = Counter(list_n).most_common(2)
    if mode[0][1] != mode[1][1]:
        modesec = mode[0][0]
    else:
        modesec = mode[1][0]
print(round(sum/n))
print(list_n[n//2])
print(modesec)
print(big-small)