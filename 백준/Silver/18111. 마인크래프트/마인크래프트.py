import sys
n, m, b = map(int, sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

result = 2**31
for a in range(257):
    time = 0
    block = b
    for i in range(n):
        for j in range(m):
            num = arr[i][j]
            if num > a:
                time += 2*(num-a)
                block+=(num-a)
            elif num < a:
                time += (a- num)
                block -= (a- num)
    if block>=0 and result > time:
        result = time
        height = a
    elif block>=0 and result == time:
        if a> height:
            height =a
print(result, height)
