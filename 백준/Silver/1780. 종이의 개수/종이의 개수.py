def paper(a, b, n):
    global mone, zero, one
    color = field[a][b]
    for i in range(a, a+n):
        for j in range(b, b+n):
            if color != field[i][j]:
                paper(a, b, n//3)
                paper(a + n//3, b, n//3)
                paper(a + 2 * n//3, b, n//3)
                paper(a, b + n//3, n//3)
                paper(a, b + 2 * n//3, n//3)
                paper(a + n//3, b + n//3, n//3)
                paper(a + 2* n//3, b + n//3, n//3)
                paper(a + n//3, b + 2*n//3, n//3)
                paper(a + 2* n//3, b + 2*n//3, n//3)
                return
    if color == 0:
        zero += 1
    elif color == 1:
        one += 1
    else:
        mone += 1

global mone, zero, one
mone = 0
zero = 0
one = 0
n = int(input())
field = [list(map(int,input().split())) for _ in range(n)]
paper(0, 0, n)
print(mone)
print(zero)
print(one)