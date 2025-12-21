def solution(n):
    num_list = list(map(int, str(n)))
    num_list.sort()
    num_list.reverse()
    
    answer = int(''.join(map(str, num_list)))
    return answer