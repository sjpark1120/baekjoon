import sys
t = int(sys.stdin.readline())
n = [0] * 301
sum = 0
for i in range(1, t+1):
    n[i] = int(sys.stdin.readline())
    sum += n[i]
arr = [0] * 301
arr[1] = n[1]
arr[2] = n[2]
arr[3] = n[3]
for i in range(4, t+1):
    arr[i] = min(arr[i - 2], arr[i - 3]) + n[i]
print(sum - min(arr[t-1], arr[t-2]))