from collections import deque
import sys
t = int(sys.stdin.readline())
for i in range(t):
    p = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")
    queue = deque(arr)
    if n == 0:
        queue =deque()
    reverse = 0
    err = 0
    for j in p:
        if j == 'R':
            if reverse == 0:
                reverse = 1
            else:
                reverse = 0
        elif j == 'D':
            if len(queue) == 0:
                err = 1
                break
            if reverse == 0:
                queue.popleft()
            else:
                queue.pop()

    len_q = len(queue)
    if err == 1:
        print('error')
    elif reverse == 0:
        print('[', end='')
        for j in range(len_q):
            print(queue.popleft(), end='')
            if j != len_q-1:
                print(',', end='')
        print(']')
    elif reverse == 1:
        print('[', end='')
        for j in range(len_q):
            print(queue.pop(), end='')
            if j != len_q-1:
                print(',', end='')
        print(']')