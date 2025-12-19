
def solution(array, commands):
    answer = []
    for com in commands:
        sliced_array = array[com[0]-1:com[1]]
        sorted_array = sorted(sliced_array)
        answer.append(sorted_array[com[2]-1])
    
    return answer