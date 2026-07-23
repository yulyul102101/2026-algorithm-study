def solution(myString):
    answer = []
    c = 0
    for i in myString:
        if i=='x': answer.append(c);c=0
        else: c+=1
        
    answer.append(c)
    return answer