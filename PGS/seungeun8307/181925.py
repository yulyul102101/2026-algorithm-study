def solution(numLog):
    answer = ''
    
    b = numLog[0]
    for i in numLog[1:]:
        if i-b==1: answer += 'w'
        if i-b==-1: answer += 's'
        if i-b==10: answer += 'd'
        if i-b==-10: answer += 'a'
        b = i
        
    return answer