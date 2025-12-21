def solution(n, lost, reserve):
    check = 0
    lost.sort()
    reserve.sort()
    remove_list = []
    
    for i in lost:
        if i in reserve:
            remove_list.append(i)
    
    for r in remove_list:
        lost.remove(r)
        reserve.remove(r)
    
    for l in lost:
        if l-1 in reserve:
            reserve.remove(l-1)
            check += 1
            continue
        elif l+1 in reserve:
            reserve.remove(l+1)
            check += 1
            continue
        
    answer = n - len(lost) + check
    return answer