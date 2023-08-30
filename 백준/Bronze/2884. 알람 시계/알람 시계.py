h, m = map(int, input().split())
if m >= 45:
    m -= 45
    print("{0} {1}".format(h, m))
else:
    if h == 0:
        h = 23
        m += 15
        print("{0} {1}".format(h, m))
    else:
        h -= 1
        m += 15
        print("{0} {1}".format(h, m))