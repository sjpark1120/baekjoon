import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    y_socre = 0
    k_socre = 0
    for j in range(9):
        y, k = map(int, input().split())
        y_socre += y
        k_socre += k

    if y_socre > k_socre:
        print("Yonsei")
    elif y_socre < k_socre:
        print("Korea")
    else:
        print("Draw")
