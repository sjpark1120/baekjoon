def solution(board, moves):
    stack = []
    answer = 0
    for i in moves:
        for b in range(len(board)):
            if board[b][i-1] != 0:
                if stack and stack[-1] == board[b][i-1]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[b][i-1])
                board[b][i-1] = 0
                break
            
    return answer