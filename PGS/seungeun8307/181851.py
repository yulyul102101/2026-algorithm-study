def solution(rank, attendance):
    c = [(r, i) for i, (r, a) in enumerate(zip(rank, attendance)) if a]
    
    c.sort()
    i1, i2, i3 = c[0][1], c[1][1], c[2][1]
    return 10000*i1 + 100*i2 + i3