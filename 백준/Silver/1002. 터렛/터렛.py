t = int(input())
for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if r1> r2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        r1, r2 = r2, r1
    dis =((x1 - x2) ** 2 + (y1 - y2) ** 2)**(1/2)
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    elif r1+r2 == dis:
        print(1)
    elif r1+r2 < dis:
        print(0)
    elif r2 == dis + r1:
        print(1)
    elif r2 > dis + r1:
        print(0)
    elif dis- r1 < r2 < dis+ r1:
        print(2)