import sys
input = sys.stdin.readline

while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break

    base = h*h + w*w

    ans = None

    for nh in range(1, 151):
        for nw in range(nh+1, 151):
            val = nh*nh + nw*nw

            if val > base or (val == base and nh > h):
                if ans is None:
                    ans = (nh, nw)
                else:
                    ah, aw = ans
                    aval = ah*ah + aw*aw

                    if (val < aval) or (val == aval and nh < ah):
                        ans = (nh, nw)

    print(ans[0], ans[1])