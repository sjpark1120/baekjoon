n = int(input())
find = 0
for i in range(n):
    sum = i
    num = i
    while(i > 0):
        sum += i % 10
        i = i//10
    if sum == n:
        print(num)
        find = 1
        break
if find == 0:
    print(0)