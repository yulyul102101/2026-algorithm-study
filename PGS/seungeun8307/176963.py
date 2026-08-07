def solution(name, yearning, photo):
    answer = []
    map = {n: yearning[i] if i<len(yearning) else 0 for i, n in enumerate(name)}
    
    for pt in photo:
        tot = 0
        for ps in pt:
            tot += map.get(ps, 0)
        answer.append(tot)
    return answer 