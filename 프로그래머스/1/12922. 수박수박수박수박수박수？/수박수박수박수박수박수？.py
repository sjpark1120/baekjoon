def solution(n):
    arr =['수', '박']
    answer = ''
    for i in range(n):
        answer += (arr[i%2])
    return answer