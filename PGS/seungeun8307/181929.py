def solution(num_list):
    mu = 1
    for i in num_list:
        mu *= i
    
    sm = sum(num_list)**2

    return 1 if mu<sm else 0