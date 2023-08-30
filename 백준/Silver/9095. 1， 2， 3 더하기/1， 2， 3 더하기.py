import sys
t = int(sys.stdin.readline())
for k in range(t):
    n = int(sys.stdin.readline())
    arr = [0]*1000001
    arr[1] = 1
    arr[2] = 2
    arr[3] = 4
    for i in range(4, n+1):
        arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]
    print(arr[n])