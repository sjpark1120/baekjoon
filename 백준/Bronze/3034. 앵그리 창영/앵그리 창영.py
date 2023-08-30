import sys
n, w, h = map(int, sys.stdin.readline().split())
diagonal = w**2 + h**2
for i in range(n):
    length = int(sys.stdin.readline())
    if length**2 > diagonal:
        print("NE")
    else:
        print("DA")
