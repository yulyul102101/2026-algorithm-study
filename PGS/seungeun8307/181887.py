def solution(num_list):
    o, no = 0, 0
    for i, v in enumerate(num_list):
        if i%2==0: no+=v
        else: o+=v
    return max(o, no)