import sys
n = int(sys.stdin.readline())
num = 0
arr = [0] * 15000
a = 0
for i in range(3000000):
    num += 1
    n_list = list(map(int, str(num)))
    for j in range(len(n_list)-2):
        if n_list[j] == 6 and n_list[j+1] == 6 and n_list[j+2]==6:
            arr[a] = num
            a += 1
            break
print(arr[n-1])