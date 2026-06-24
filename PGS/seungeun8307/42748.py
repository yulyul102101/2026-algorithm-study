def solution(array, commands):
    answer = []
    for row in range(len(commands)):
        a = array[commands[row][0]-1:commands[row][1]]
        a.sort()
        answer.append(a[commands[row][2]-1])
    return answer