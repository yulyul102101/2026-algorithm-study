def solution(num):
    answer = 0
    i = 0
    if num==1: return 0

    while i<500:
        if num==1: answer = i; break
        elif num%2==0: num//=2;i+=1
        else: num = num*3+1;i+=1
        
    return answer if answer else -1