n = int(input())
def hanoi(x,a, b, c):
    if x == 1:
        print("{} {}".format(a, c))
    else:
        hanoi(x-1, a, c, b)
        print("{} {}".format(a, c))
        hanoi(x-1, b, a, c)
print(2**n - 1)
hanoi(n, 1, 2, 3)