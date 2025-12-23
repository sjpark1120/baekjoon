def solution(progresses, speeds):
    stack = []
    answer = []
    check = 0
    for i in range(len(progresses)):
        due_day = (100 - progresses[i]) // speeds[i]
        if (100 - progresses[i]) % speeds[i]:
            due_day += 1
        stack.append(due_day)
    
    prev = 0
    check = 0
    for i in range(len(stack)):
        if i == 0:
            prev = stack[i]
            check += 1
        elif prev >= stack[i]:
            check += 1
        else: 
            answer.append(check)
            prev = stack[i]
            check = 1
    answer.append(check)  
    return answer