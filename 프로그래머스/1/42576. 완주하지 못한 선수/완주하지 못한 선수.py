def solution(participant, completion):
    participant.sort()
    completion.sort()
    for co in range(len(completion)):
        if participant[co] != completion[co]:
            return participant[co]
    return participant[-1]