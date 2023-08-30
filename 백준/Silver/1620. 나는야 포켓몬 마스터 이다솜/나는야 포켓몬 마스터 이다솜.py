import sys
n, m = map(int, sys.stdin.readline().split())
namelist = dict()
result = []
for i in range(n):
    name = str(sys.stdin.readline().rstrip())
    namelist[name] = i+1
listname = {v:k for k,v in namelist.items()}
for i in range(m):
    nameornum = str(sys.stdin.readline().rstrip())
    if namelist.get(nameornum, 0) != 0:
        print(namelist[nameornum])
    else:
        print(listname[int(nameornum)])