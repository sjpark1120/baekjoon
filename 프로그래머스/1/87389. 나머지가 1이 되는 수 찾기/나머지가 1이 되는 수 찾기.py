def solution(n):
    answer = n-1
    for i in range(n-1):
        if n % (i+1) == 1:
            answer = i+1
            break
    return answer