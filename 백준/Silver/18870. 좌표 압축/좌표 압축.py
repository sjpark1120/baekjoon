import sys
n = int(sys.stdin.readline())
arr = [0]*n
arr = list(map(int, sys.stdin.readline().split()))
copyarr = arr.copy()
newarr=list(set(copyarr))
newarr.sort()
arrdict={i:v for v,i in enumerate(newarr)}
for i in arr:
    print(arrdict[i], end = ' ')