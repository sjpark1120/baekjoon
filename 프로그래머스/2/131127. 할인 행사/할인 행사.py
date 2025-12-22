def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-9):
        arr = discount[i:i+10]
        check = 1
        for j in range(len(want)):
            if number[j] > arr.count(want[j]):
                check = 0
        if check == 1:
            answer += 1           
    return answer