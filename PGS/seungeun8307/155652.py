def solution(s, skip, index):
    answer = ''
    abc = [c for c in 'abcdefghijklmnopqrstuvwxyz' if c not in skip]
    
    for c in s:
        n = abc.index(c)
        nw = (n+index)%len(abc)
        answer += abc[nw]
    
    return answer