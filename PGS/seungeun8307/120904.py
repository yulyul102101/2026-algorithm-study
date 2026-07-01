def solution(num, k):
    k, num = str(k), str(num)
    
    try:
        return num.index(k)+1
    except ValueError:
        return -1