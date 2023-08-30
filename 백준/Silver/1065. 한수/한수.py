tmp = [0] * 1001
for i in range(1000):
    j = i+1
    if j<100:
        tmp[j]=1
    elif j==1000:
        break
    else:
        a =j//100
        b =j//10%10
        c =j%10
        if (a-b) == (b-c):
            tmp[j]=1

n =int(input())
sum = 0
for i in range(n):
    j =i+1
    if tmp[j] ==1:
        sum += 1
print(sum)