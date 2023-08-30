import sys
arr = []
sum = 0
for i in range(9):
    a = int(sys.stdin.readline())
    arr.append(a)
    sum += a
arr.sort()
for i in range(9):
    for j in range(i+1, 9):
        sum_ = sum
        sum_ = sum_ - arr[i] - arr[j]
        if sum_ == 100:
            numi = arr[i]
            numj = arr[j]
            break
for i in range(9):
    if arr[i] == numi or arr[i] == numj:
        continue
    else:
        print(arr[i])
