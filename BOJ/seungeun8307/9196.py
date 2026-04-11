import sys
import math

rects = []
for h in range(1,151):
    for w in range(h+1,151):
        rects.append((h,w))

rects.sort(key=lambda r: (r[0]**2 + r[1]**2, r[0])) 

index = {r: i for i, r in enumerate(rects)}

while(True):
    h, w = map(int,sys.stdin.readline().split())
    if h == 0 and w == 0: break
    i = index[(h,w)]
    nh, nw = rects[i+1]
    print(nh,nw)