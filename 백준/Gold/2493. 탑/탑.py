import sys
n = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().split()))
signal = []
stack = []

for i in range(n):
    while stack:
        if stack[-1][1] > tower[i]:
            signal.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:
        signal.append(0)
    stack.append([i, tower[i]])
    
for i in signal:
    print(i, end=' ')
