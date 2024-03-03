n = int(input())
D = [0 for _ in range(n+2)]
D[1] = 1
D[2] = 3

for i in range(3, n+1):
  D[i] = (D[i-1] + D[i-2]*2)%10007
print(D[n])