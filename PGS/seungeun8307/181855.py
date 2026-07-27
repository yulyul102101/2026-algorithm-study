import collections

def solution(strArr):
    ls = [len(s) for s in strArr]
    
    answer = collections.Counter(ls)
    
    return max(answer.values())