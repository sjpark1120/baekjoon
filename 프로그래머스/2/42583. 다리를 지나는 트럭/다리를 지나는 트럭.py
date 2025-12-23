def solution(bridge_length, weight, truck_weights):
    queue = [0 for _ in range(bridge_length)]
    time = 0
    kg = 0
    while truck_weights:
        time += 1
        kg -= queue.pop(0)
        if kg + truck_weights[0] <= weight:
            tw =truck_weights.pop(0)
            queue.append(tw)
            kg += tw
        else:
            queue.append(0)
    while queue:
        time += 1
        queue.pop(0)
    return time