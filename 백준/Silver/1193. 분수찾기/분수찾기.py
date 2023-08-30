x = int(input())
n = 1
while(x > n*(n+1)/2):
    n += 1
k = x - n*(n+1)//2
if n%2 == 0: # 짝
    top = n +k
    bottom = 1 -k
else:
    top = 1-k
    bottom = n+k
print("{}/{}".format(top, bottom))