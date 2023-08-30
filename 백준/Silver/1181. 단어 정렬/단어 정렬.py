import sys
n = int(sys.stdin.readline())
arr = [0]*n
for i in range(n):
    arr[i] = input()
arr.sort(key = lambda x: (len(x),x))
result = []
for i in arr:
    if i not in result:
        result.append(i)

for i in range(len(result)):
    print(result[i])
