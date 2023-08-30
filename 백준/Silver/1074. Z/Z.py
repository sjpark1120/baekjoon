import sys
def func(n, r, c):
    half = 2**(n-1)
    if n == 0:
        return 0
    if r < half and c < half : #1번사각형
        return func(n-1, r, c)
    elif r < half and c >= half:
        return func(n-1, r, c - half) + half*half
    elif r >= half and c < half:
        return func(n-1, r- half, c) + half*half*2
    else:
        return func(n-1, r - half, c - half) + half*half*3
n, r, c = (map(int, sys.stdin.readline().split()))
print(func(n,r,c))