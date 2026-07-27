def solution(myStr):
    sp = ['a','b','c']
    t = ''
    answer = []
    for i in myStr:
        if i in sp:
            if t!='':answer.append(t);t=''
        else:
            t += i
        
    answer.append(t)
    return ['EMPTY'] if answer == [''] else answer