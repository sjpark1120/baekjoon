n = int(input())
f = int(input())
nn = n - (n%100)
for i in range(100):
    num = nn + i
    if num % f == 0:
        print(str(i).zfill(2))
        break