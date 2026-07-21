def ft(arr):
    new_arr = []
    for x in arr:
        if x >= 50 and x % 2 == 0:
            new_arr.append(x // 2)
        elif x < 50 and x % 2 != 0:
            new_arr.append(x * 2 + 1)
        else:
            new_arr.append(x)
    return new_arr


def solution(arr):
    answer = 0
    now, nex= arr, ft(arr)
    while now != nex:
        now = nex
        nex = ft(now)
        answer += 1
        
    return answer