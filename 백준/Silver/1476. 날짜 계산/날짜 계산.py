import sys

input = sys.stdin.readline

e, s, m = map(int, input().split())
count = 0

while 1:
    count_e = count % 15 + 1
    count_s = count % 28 + 1
    count_m = count % 19 + 1

    if e == count_e and s == count_s and m == count_m:
        break

    count += 1

print(count + 1)
