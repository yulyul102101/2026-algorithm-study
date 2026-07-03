def solution(my_string):
    t = my_string.split()
    
    answer = int(t[0])
    for i in range(1, len(t), 2):
        op = t[i]
        num = int(t[i+1])
        
        if op == '+':
            answer += num
        elif op == '-':
            answer -= num
            
    return answer