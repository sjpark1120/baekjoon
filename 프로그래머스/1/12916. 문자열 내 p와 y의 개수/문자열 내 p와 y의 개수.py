def solution(s):
    y = 0
    p = 0
    for char in s:
        if char == "p" or char == "P":
            p+= 1
        elif char == "y" or char == "Y":
            y+= 1
        
    return y==p