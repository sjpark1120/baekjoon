import sys

input = sys.stdin.readline

n = int(input())
s = list(input().strip())

c_count = 0
for ch in s:
    if ch == "C":
        c_count += 1

other_count = n - c_count
print(-(-c_count // (other_count + 1)))
