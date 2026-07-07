import collections

def solution(array):
    c = collections.Counter(array)
    mf = max(c.values())
    ms = [i for i, j in c.items() if j==mf]
    
    return ms[0] if len(ms) == 1 else -1