n = int(input())
std = list(input())
for i in range(n-1):
    name = list(input())
    for j in range(len(std)):
        if std[j] != name[j]:
            std[j] = '?'
for k in std:
    print(k, end='')