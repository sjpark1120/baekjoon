def promising(level):
    for i in range(level):
        if cols[i] == cols[level] or abs(level - i) == abs(cols[level] - cols[i]):
            return False
    return True

def queens(level):
    global counter
    if level == n:
        counter += 1
        return
    else:
        for i in range(n):
            cols[level] = i
            if promising(level):
                queens(level+1)

n = int(input())
cols = [0] * (n)
counter = 0
queens(0)
print(counter)