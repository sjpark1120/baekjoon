import sys
word = list(sys.stdin.readline().rstrip())
stack = []
start = 0
cnt = 0
for i in range(len(word)):
    if word[i] == '(':
        stack.append(word[i])
        start += 1
    elif word[i] == ')' and word[i-1] == '(':
        stack.pop() 
        start -= 1
        cnt += len(stack)
    elif word[i] == ')':
        stack.pop()
print(cnt + start)