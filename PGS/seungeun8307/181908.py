def solution(my_string, is_suffix):
    ss = []
    for i in range(len(my_string)):
        ss.append(my_string[i:])
    
    return 1 if is_suffix in ss else 0