def solution(name, yearning, photo):
    memory = {}
    answer = []
    for n, y in zip(name, yearning):
        memory[n] = y
    for p in photo:
        print(p)
        score = 0
        for name in p:
            if name in memory:
                score += memory[name]
        answer.append(score)
    return answer