def solution(k, d):
    answer = 0
    
    for i in range(d//k + 1):
        a = int((d**2 - (k*i)**2) ** 0.5 // k)
        answer += a + 1
        
    return answer