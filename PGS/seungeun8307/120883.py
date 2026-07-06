def solution(id_pw, db):
    
    for users in db:
        if id_pw[0] == users[0]:
            if id_pw[1] == users[1]:
                return  'login'
            else: 
                return 'wrong pw'
    return 'fail'