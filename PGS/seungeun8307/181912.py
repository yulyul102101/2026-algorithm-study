def solution(intStrs, k, s, l):
    answer = []
    st = list(intStrs)
    for i in st:
        n = int(i[s:s+l])
        if n > k: answer.append(n) 
    return answer