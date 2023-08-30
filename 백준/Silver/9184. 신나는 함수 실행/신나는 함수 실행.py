def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return 1048576
    elif a < b < c:
        return 2**a
    elif arr[a][b][c] > 0:
        return arr[a][b][c]
    else:
        arr[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        return arr[a][b][c]


import sys
while(True):
    a, b, c = map(int, sys.stdin.readline().split())
    arr = [[[0 for k in range(21)] for j in range(21)] for i in range(21)]
    if a == -1 and b == -1 and c == -1:
        break
    print("w({}, {}, {}) = {}".format(a, b, c, w(a, b, c)))