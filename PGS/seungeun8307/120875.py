def solution(dots):
    def s(a, b):
        if a[0] == b[0]:
            return None
        return (b[1]-a[1]) / (b[0]-a[0])
    
    p = [
        (dots[0], dots[1], dots[2], dots[3]),
        (dots[0], dots[3], dots[1], dots[2]),
        (dots[0], dots[2], dots[3], dots[1])
    ]
    
    for a, b, c, d in p:
        if s(a, b) == s(c, d): return 1
    
    return 0