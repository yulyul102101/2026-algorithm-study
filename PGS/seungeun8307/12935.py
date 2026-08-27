def solution(arr):
    arr.pop(arr.index(min(arr)))
    answer = arr
    return answer if answer else [-1]