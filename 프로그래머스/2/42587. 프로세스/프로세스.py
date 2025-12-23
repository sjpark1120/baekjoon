def solution(priorities, location):
    order = 1
    location_arr = [i for i in range(len(priorities))]
    while priorities:
        priorities_pop = priorities.pop(0)
        location_arr_pop = location_arr.pop(0)
        if len(priorities) == 0:
            break
        elif max(priorities) > priorities_pop:
            priorities.append(priorities_pop)
            location_arr.append(location_arr_pop)
        elif location_arr_pop == location:
            break
        else:
            order += 1
            
    return order