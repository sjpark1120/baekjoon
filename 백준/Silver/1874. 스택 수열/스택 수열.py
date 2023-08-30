import sys
n = int(sys.stdin.readline())
solve = []
check = 0
p = 1
stack = []
for i in range(n):
    number = int(sys.stdin.readline())
    while(p <= number):
        stack.append(p)
        solve.append("+")
        p+=1
    if stack[-1] == number:
        stack.pop()
        solve.append("-")
    else:
        print("NO")
        check =1
        break
if check == 0:
    for i in solve:
        print(i)