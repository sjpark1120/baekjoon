import sys
n = int(sys.stdin.readline())
namelist = dict()
for i in range(n):
    a, b = map(str, sys.stdin.readline().split())
    if b == 'enter':
        namelist[a] = 'enter'
    else:
        del namelist[a]
namelist = sorted(namelist.keys(), reverse=True)
for key in namelist:
    print(key)