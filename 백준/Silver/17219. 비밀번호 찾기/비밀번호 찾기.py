import sys
n, m = (map(int, sys.stdin.readline().split()))
dic ={}
for i in range(n):
    web, password = sys.stdin.readline().split()
    dic[web] = password
for i in range(m):
    forgetweb = sys.stdin.readline().rstrip()
    print(dic[forgetweb])