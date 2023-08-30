import sys
n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(sys.stdin.readline())
counter = []
for i in range(n-7):
    for j in range(m-7):
        repaint1 = 0
        repaint2 = 0
        for a in range(i,i+8):
            for b in range(j,j+8):
                if (a+b)%2 == 0:
                    if arr[a][b] != 'W':
                        repaint1 += 1
                    if arr[a][b] != 'B':
                        repaint2 += 1
                else:
                    if arr[a][b] != 'B':
                        repaint1 += 1
                    if arr[a][b] != 'W':
                        repaint2 += 1
        counter.append(min(repaint1, repaint2))
print(min(counter))