a = int(input())
n = a
cycle = 0
while(True):
    cycle += 1
    sum = n//10 + n%10
    n= n%10*10 + sum%10
    if (n == a):
        break
print(cycle)