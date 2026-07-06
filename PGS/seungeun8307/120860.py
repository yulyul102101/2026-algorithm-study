def solution(dots):
    wid, hei = [], []
    
    for i in dots:
        wid.append(i[0])
        hei.append(i[1])
        
    answer = abs(
        (max(wid)-min(wid)
        )*(
        max(hei)-min(hei)))
    return answer