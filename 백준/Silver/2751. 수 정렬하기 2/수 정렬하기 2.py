n = int(input())
list = [0] * n
for i in range(n):
    list[i] = int(input())
list.sort()
for i in range(n):
    print(list[i])