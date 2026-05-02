def solution(t, p):
    answer = 0
    p_num = int(p)
    length = len(p)
    
    for i in range(len(t) - length + 1):
        sub = t[i:i+length]
        if int(sub) <= p_num:
            answer += 1
            
    return answer