def paper(a, b, n):
    color = field[a][b]
    for i in range(a, a+n):
        for j in range(b, b+n):
            if color != field[i][j]:
                print("(", end="")
                paper(a, b, n//2)
                paper(a, b + n//2, n//2)
                paper(a + n//2, b, n//2)
                paper(a + n//2, b + n//2, n//2)
                print(")", end="")
                return
    if color == 0:
        print("0", end="")
    else:
        print("1", end="")

n = int(input())
field = [list(map(int,input())) for _ in range(n)]
paper(0, 0, n)