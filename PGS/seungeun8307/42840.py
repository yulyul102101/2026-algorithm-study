def solution(answers):
    answer = []
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    
    score = [0,0,0]
    
    for i, ans in enumerate(answers):
        if ans == a[i%len(a)]: score[0] += 1
        if ans == b[i%len(b)]: score[1] += 1
        if ans == c[i%len(c)]: score[2] += 1
        
    m = max(score)
    for i, s in enumerate(score):
        if s == m:
            answer.append(i+1)
    
    return answer