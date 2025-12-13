import sys

input = sys.stdin.readline

s = list(input().rstrip())
stack = []
flag = 0

for i in s:
    if i == ">":
        flag = 0
        stack.append(i)
        print("".join(stack), end="")
        stack.clear()
    elif (i == " " or i == "<") and flag == 0:
        while stack:
            print(stack.pop(), end="")
        print(i, end="")
        if i == "<":
            flag = 1
    else:
        stack.append(i)
while stack:
    print(stack.pop(), end="")