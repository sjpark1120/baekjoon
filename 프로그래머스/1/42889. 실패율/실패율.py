def solution(N, stages):
    stage_user = [0 for _ in range(N+1)]
    persent = [[0 for _ in range(2)] for _ in range(N)]
    answer = []
    
    for s in stages:
        stage_user[s-1] += 1
    for i in range(N):
        persent[i][0] = stage_user[i] / sum(stage_user[i:]) if sum(stage_user[i:]) != 0 else 0 
        persent[i][1] = i+1
    persent.sort(key=lambda x:x[0], reverse=True)
    
    for p in persent:
        answer.append(p[1])
    return answer