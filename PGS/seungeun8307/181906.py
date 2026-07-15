def solution(my_string, is_prefix):
    ss = []
    for i in range(len(my_string)):
        ss.append(my_string[:i+1])
        
    return 1 if is_prefix in ss else 0