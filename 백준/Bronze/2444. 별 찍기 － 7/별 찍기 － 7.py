import sys
a = int(sys.stdin.readline())
for i in range(a):
    print(" "*(a-i-1) + "*"*(i*2+1))
for i in range(1, a):
    print(" "*(i) + "*"*((a-i)*2-1))