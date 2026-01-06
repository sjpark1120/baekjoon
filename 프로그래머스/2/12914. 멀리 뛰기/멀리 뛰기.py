def solution(n):
    arr = [0 for _ in range(n+2)]
    for i in range(n-1):
        arr[i+1] += 1+arr[i]
        if i == n-1:
            break
        arr[i+2] += 1+arr[i]

    answer = (arr[n] +1) % 1234567
    return answer