def solution(lines):
    mi = min(start for start, end in lines)
    ma = max(end for start, end in lines)
    
    over = 0
    for i in range(mi, ma):
        count = 0
        for start, end in lines:
            if start <= i and end > i:
                count += 1
        if count >= 2:
            over += 1
    
    return over