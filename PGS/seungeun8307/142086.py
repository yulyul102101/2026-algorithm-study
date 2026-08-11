def solution(s):
    answer = []
    ls = {}
    
    for i, c in enumerate(s):
        if c in ls:
            answer.append(i-ls[c])
        else: answer.append(-1)
        ls[c] = i
        
    return answer