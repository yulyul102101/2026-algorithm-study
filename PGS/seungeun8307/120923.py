def solution(num, total):
    s = (total - (num * (num-1)) // 2) // num
    return [s + i for i in range(num)]