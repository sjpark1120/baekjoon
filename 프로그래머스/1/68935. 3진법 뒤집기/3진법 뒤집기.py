def solution(n):
    rb = ''

    while n > 0:
        n, mod = divmod(n, 3)
        rb += str(mod)

    return int(rb,3)