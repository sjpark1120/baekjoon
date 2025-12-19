def solution(s):
    stack = []
    
    for ch in s:   
        if ch == "(":
            stack.append(ch)
        else:
            if not stack:
                return False
            elif stack.pop() != "(":
                return False
    if stack:
        return False
    return True