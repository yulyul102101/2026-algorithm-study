def solution(arr, n):
    answer = arr
    if len(arr) %2==0: 
        for i in range(len(answer)):
            if i%2!=0: answer[i]+=n
    else:
        for i in range(len(answer)):
            if i%2==0: answer[i]+=n
            
    return answer