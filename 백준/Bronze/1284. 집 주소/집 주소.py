while True:
    n = list(input())
    cnt = 0
    if n == ['0']:
        break
    for i in n:
        if i == '1':
            cnt += 2
        elif i == '0':
            cnt += 4
        else:
            cnt += 3
    print(cnt + len(n) + 1)