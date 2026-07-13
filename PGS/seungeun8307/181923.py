def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        c = [x for x in arr[s:e+1] if x>k]
        answer.append(min(c) if c else -1)
    return answer