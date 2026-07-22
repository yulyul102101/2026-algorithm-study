def solution(strArr):
    answer = []
    for i, s in enumerate(strArr):
        if i%2!=0: answer.append(s.upper())
        else: answer.append(s.lower())
    return answer