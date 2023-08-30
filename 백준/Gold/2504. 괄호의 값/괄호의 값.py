import sys
word = list(sys.stdin.readline().rstrip())
stack = []
error = 0
tmp = 1
num = 0
for i in range(len(word)):
    if word[i] == '(':
        stack.append(word[i])
        tmp *= 2
    elif word[i] == '[':
        stack.append(word[i])
        tmp *=3
    elif word[i] == ')':
        if len(stack) == 0:
            error = 1
            break
        x = stack.pop()
        if x != '(':
            error = 1
            break
        if word[i-1] == '(':
            num += tmp
        tmp //= 2
    elif word[i] == ']':
        if len(stack) == 0:
            error = 1
            break
        x = stack.pop()
        if x != '[':
            error = 1
            break
        if word[i-1] == '[':
            num += tmp
        tmp //= 3
if len(stack) != 0:
    error = 1
if error == 1:
    print(0)
else:
    print(num)