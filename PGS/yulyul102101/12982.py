def solution(d, budget):
    d.sort()
    
    count = 0
    total = 0
    
    for cost in d:
        total += cost
        if total > budget:
            break
        count += 1
        
    return count