def solution(num_list):
    answer = 0
    o, no = '', ''
    for i in num_list:
        if i%2!=0: o += str(i)
        else: no += str(i)
    
    return int(o) + int(no)