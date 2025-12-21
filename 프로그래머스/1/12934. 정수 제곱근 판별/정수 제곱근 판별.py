import math

def solution(n):
    k = math.sqrt(n)
    if k.is_integer() and k > 0:
        return int((k+1)**2)
    else:
        return -1