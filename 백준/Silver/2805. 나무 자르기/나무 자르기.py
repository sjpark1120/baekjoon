import sys
n, m =map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
start = 0
end = 1000000000
while(start<end):
    mid = (start+end+1)//2
    sum = 1
    for i in range(n):
        if arr[i] > mid:
            sum+=arr[i]-mid
    if sum>m:
        start = mid
    else:
        end = mid -1
print(start)