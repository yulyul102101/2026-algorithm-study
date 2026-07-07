def solution(chicken):
    p = 0
    
    while chicken >=10:
        new = chicken//10
        p += new
        chicken = chicken%10 + new
        
    return p