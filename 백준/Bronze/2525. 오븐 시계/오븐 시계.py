h, m =map(int, input().split())
n = int(input())
if m+n < 60:
    m += n
else:
    h += (m+n)//60
    m = (m+n)%60
    if h>23:
        h -= 24
print("{0} {1}".format(h, m))