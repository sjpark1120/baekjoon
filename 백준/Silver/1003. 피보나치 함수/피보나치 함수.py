zero = [1, 0, 1]
one = [0, 1, 1]
def fibonacci(x):
    length = len(zero)
    if x >= length:
        for i in range(length, x+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print('{} {}'.format(zero[x], one[x]))
n = int(input())
for i in range(n):
    x = int(input())
    fibonacci(x)