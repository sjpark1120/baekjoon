a, b, c = map(int, input().split())
d = int(input())
c += d
if c > 59:
    b += int(c / 60)
    c = c % 60
if b > 59:
    a += int(b / 60)
    b = b % 60
if a > 23:
    a = a % 24

print(a, b, c)