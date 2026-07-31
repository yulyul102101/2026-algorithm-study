def solution(picture, k):
    answer = []
    for i in picture:
        t = ''
        for j in i:
            t += j*k
        for _ in range(k):
            answer.append(t)
    return answer