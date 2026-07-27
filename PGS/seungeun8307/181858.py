def solution(arr, k):
    answer = []
    s = set()
    
    for i in arr:
        if i not in s:
            answer.append(i)
            s.add(i)
        if len(answer) == k:
            break
            
    while len(answer)<k:
        answer.append(-1)
        
    return answer