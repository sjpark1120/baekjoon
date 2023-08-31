import sys
set = dict()
arr = list(str(sys.stdin.readline().strip()))
for i in range(len(arr)):
    string =''
    for j in range(i, len(arr)):
        string+=arr[j]
        set[string] = 1
print(len(set))