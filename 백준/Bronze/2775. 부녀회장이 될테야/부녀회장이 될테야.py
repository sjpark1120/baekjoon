def resident():
    for j in range(14):
        list[0][j+1] = j+1
    for f in range(14):
        for r in range(14):
            for m in range(r+1):
                list[f+1][r+1] += list[f][r+1-m]
list = [[0]*15 for _ in range(15)]
t = int(input())
resident()
for i in range(t):
    k = int(input())
    n = int(input())
    print(list[k][n])