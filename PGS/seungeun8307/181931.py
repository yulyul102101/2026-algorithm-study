def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        t = a+d*i
        if included[i]: answer+=t
    return answer