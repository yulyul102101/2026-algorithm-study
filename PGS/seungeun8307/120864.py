def solution(my_string):
    answer = 0
    nums = []
    cn = ''
    
    for i in my_string:
        if i.isdigit(): cn+= i
        else:
            if cn:
                nums.append(int(cn))
                cn = ''
                
    if cn:
        nums.append(int(cn))
        
    answer = sum(nums)
    
    return answer