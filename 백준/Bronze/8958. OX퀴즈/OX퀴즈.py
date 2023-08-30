n = int(input())
for k in range(n):
    a = list((input().rstrip('\n')))
    score = 0
    bonus = 0
    for i in range(len(a)):
        if a[i] == 'O':
            bonus += 1
            score += bonus
        else:
            bonus = 0
    print(score)