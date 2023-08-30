import sys
a = int(sys.stdin.readline())
for i in range(a):
    print("*"*(i+1) + " "*((a-i-1)*2) + "*"*(i+1))
for i in range(1, a):
    print("*"*(a-i) + " "*((i)*2) + "*"*(a-i))