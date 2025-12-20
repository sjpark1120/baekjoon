def solution(answers):
    answer = []
        
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    a_score = 0
    b_score = 0
    c_score = 0
    
    for i in range(len(answers)):
        a_score += int(answers[i] == a[i%5])
        b_score += int(answers[i] == b[i%8])
        c_score += int(answers[i] == c[i%10])
    
    max_score = max(a_score,b_score,c_score)
    if max_score == a_score:
        answer.append(1)
    if max_score == b_score:
        answer.append(2)
    if max_score == c_score:
        answer.append(3)
    return answer