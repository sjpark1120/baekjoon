def solution(seoul):
    for p in range(len(seoul)):
        if seoul[p] == "Kim":
            return f'김서방은 {p}에 있다'
    return answer