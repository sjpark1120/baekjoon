a =int(input())
b =int(input())
c =int(input())
num = a * b * c
list = [0] *10
while(num > 0):
    list[num%10] += 1
    num = num//10
for i in range(10):
    print(list[i])