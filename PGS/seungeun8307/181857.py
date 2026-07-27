def solution(arr):
    l = len(arr)
    
    i = 1
    while i<l:
        i*=2
        
    arr.extend([0]*(i-l))
    return arr