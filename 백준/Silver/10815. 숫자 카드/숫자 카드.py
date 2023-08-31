import sys
def search(arr, a):
    start = 0
    end = len(arr) - 1
    mid = (start + end) // 2

    while (end - start >= 0):
        if arr[mid] == a:
            return mid
        elif arr[mid] < a:
            start = mid + 1
        else:
            end = mid - 1
        mid = (start + end) // 2
    return -1

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
m = int(sys.stdin.readline())
searcharr = list(map(int, sys.stdin.readline().split()))
result = []
for i in range(m):
    if search(arr, searcharr[i]) == -1:
        result.append(0)
    else:
        result.append(1)
for i in range(m):
    print(result[i], end =' ')