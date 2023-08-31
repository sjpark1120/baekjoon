import sys
n, w, l = map(int, sys.stdin.readline().split())
truck = list(map(int, sys.stdin.readline().split()))
bridge =[0] * w
time = 0
while len(bridge):
    time += 1
    bridge.pop(0)
    if truck:
        if sum(bridge) + truck[0] <= l:
            a = truck.pop(0)
            bridge.append(a)
        else:
            bridge.append(0)

print(time)