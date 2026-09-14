def solution(a, b):
    answer = 0
    for av, bv in zip(a,b):
        answer += av*bv
    return answer