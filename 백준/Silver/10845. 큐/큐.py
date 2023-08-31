import sys
n = int(sys.stdin.readline())
arr = []
sum=0
for i in range(n):
    command = sys.stdin.readline().strip().split()
    if command[0] == 'push':
        arr.append(command[1])
    elif command[0] == 'pop':
        if len(arr) == 0:
            print(-1)
        else:
            num = arr.pop(0)
            print(num)
    elif command[0] == 'size':
        print(len(arr))
    elif command[0] == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
    elif command[0] == 'back':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[len(arr)-1])