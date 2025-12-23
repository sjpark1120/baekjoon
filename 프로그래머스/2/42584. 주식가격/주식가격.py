def solution(prices):
    stack = []
    answer =[0 for _ in range(len(prices))]
    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop() 
            answer[j] = i-j
        stack.append(i)
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j
    return answer