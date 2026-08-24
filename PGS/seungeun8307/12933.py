def solution(n):
    di = sorted(str(n), reverse=True)
    answer = int(''.join(di))
    return answer