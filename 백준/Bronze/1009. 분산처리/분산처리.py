t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    if a % 10 == 0:
        com = 10
    elif b % 4 == 0:
        com = (a**4) % 10
    else:
        com = (a**(b%4)) % 10
    print(com)