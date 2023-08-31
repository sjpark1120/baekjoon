import sys
n, m = map(int, sys.stdin.readline().split())
namelist = dict()
memberlist = dict()
for a in range(n):
    teamname = str(sys.stdin.readline().rstrip())
    membernum = int(sys.stdin.readline())
    member = []
    for b in range(membernum):
        membername = str(sys.stdin.readline().rstrip())
        namelist[membername] = teamname
        member.append(membername)
    memberlist[teamname] = member
for c in range(m):
    q = str(sys.stdin.readline().rstrip())
    k = int(sys.stdin.readline())
    if k == 1:
        print(namelist[q])
    else:
        print('\n'.join(sorted(memberlist[q])))