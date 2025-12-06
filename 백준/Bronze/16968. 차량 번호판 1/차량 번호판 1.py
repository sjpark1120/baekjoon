import sys

input = sys.stdin.readline

pattern = list(input().strip())
count = 1

for index, ch in enumerate(pattern):
    if ch == "c":
        if index != 0 and pattern[index - 1] == ch:
            count *= 25
        else:
            count *= 26

    if ch == "d":
        if index != 0 and pattern[index - 1] == ch:
            count *= 9
        else:
            count *= 10

print(count)
